from django.core.management.base import BaseCommand, CommandError
from cc.models import ProxyServer, Statistic
from datetime import datetime
import commands, time, threading

class Command(BaseCommand):
    def handle(self, *args, **options):
        class Thread(threading.Thread):
            def __init__(self, ip, net_max, mem_max, period):
                self.ip = ip
                self.net_max = net_max
                self.mem_max = mem_max
                self.period = period
                threading.Thread.__init__(self)
            def run(self):
                net_in_start = float(commands.getoutput('snmpget -v 2c -c 1qaz2wsx3edc_ -Oqv %s IF-MIB::ifInOctets.2' % self.ip))
                time.sleep(1)
                net_in_stop = float(commands.getoutput('snmpget -v 2c -c 1qaz2wsx3edc_ -Oqv %s IF-MIB::ifInOctets.2' % self.ip))
                net_out_start = float(commands.getoutput('snmpget -v 2c -c 1qaz2wsx3edc_ -Oqv %s IF-MIB::ifOutOctets.2' % self.ip))
                time.sleep(1)
                net_out_stop = float(commands.getoutput('snmpget -v 2c -c 1qaz2wsx3edc_ -Oqv %s IF-MIB::ifOutOctets.2' % self.ip))
                net = ((net_in_stop - net_in_start) + (net_out_stop - net_out_start)) * 8
                net_load = (net * 100) / (2 * self.net_max * 1048576)
                cpu_load = float(commands.getoutput('snmpget -v 2c -c 1qaz2wsx3edc_ -Oqv %s UCD-SNMP-MIB::laLoad.2' % self.ip))
                mem = float(commands.getoutput('snmpget -v 2c -c 1qaz2wsx3edc_ -Oqv %s UCD-SNMP-MIB::memAvailReal.0' % self.ip).split(' ')[0])
                mem_load = 100 - (mem * 100 / 1024) / self.mem_max
                av_load = (net_load + cpu_load + mem_load) / 3
                tcp_conn = int(commands.getoutput('snmpget -v 2c -c 1qaz2wsx3edc_ -Oqv %s TCP-MIB::tcpCurrEstab.0' % self.ip))
                ProxyServer.objects.filter(ip=self.ip).update(mem_load=mem_load)
                ProxyServer.objects.filter(ip=self.ip).update(cpu_load=cpu_load)
                ProxyServer.objects.filter(ip=self.ip).update(net_load=net_load)
                ProxyServer.objects.filter(ip=self.ip).update(av_load=av_load)
                node = ProxyServer.objects.get(ip=self.ip)
                Statistic.objects.create(node=node, mem_load=mem_load, cpu_load=cpu_load, net_load=net_load, av_load=av_load, tcp_conn=tcp_conn, date=self.period)

        for node in ProxyServer.objects.filter(is_active=True):
            period = datetime.now()
            Thread(node.ip, node.net_max, node.mem_max, period).start()