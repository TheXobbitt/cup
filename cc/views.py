from django.shortcuts import render_to_response
from django.template import RequestContext
from cc.models import Statistic, Node
from datetime import *

class Stat:
    def __init__(self, node_name, period):
        start_time = datetime.now() - timedelta(hours = period)
        stats = Statistic.objects.filter(node__name = node_name).filter(date__gt = start_time)
        self.mem = [node.mem_load for node in stats]
        self.cpu = [node.cpu_load for node in stats]
        self.net = [node.net_load for node in stats]
        self.conn = [node.tcp_conn for node in stats]
        self.capt = [(node.date.year, node.date.month - 1, node.date.day, node.date.hour, node.date.minute, node.date.second) for node in stats]


def startpage(request):
    return render_to_response('startpage.html', locals(), context_instance = RequestContext(request))

def stat(request):
#    nodes_hourly = {node.name.split(' ')[1]: Stat(node.name, 1) for node in Node.objects.filter(is_active = 1)}
#    nodes_daily = {node.name.split(' ')[1]: Stat(node.name, 24) for node in Node.objects.filter(is_active = 1)}

    nodes_1_hourly = Stat('Node_1', 1)
    nodes_1_daily = Stat('Node_1', 24)
    nodes_2_hourly = Stat('Node_2', 1)
    nodes_2_daily = Stat('Node_2', 24)
    nodes_3_hourly = Stat('Node_3', 1)
    nodes_3_daily = Stat('Node_3', 24)
    nodes_4_hourly = Stat('Node_4', 1)
    nodes_4_daily = Stat('Node_4', 24)
#    test = [['new Date' + str(nodes_1_hourly.capt[n]), nodes_1_hourly.mem[n], nodes_2_hourly.mem[n], nodes_3_hourly.mem[n]] for n in xrange(len(nodes_1_hourly.capt))]

    chart_mem_hourly = [{'date': nodes_1_hourly.capt[n], 'n1': nodes_1_hourly.mem[n], 'n2': nodes_2_hourly.mem[n], 'n3': nodes_3_hourly.mem[n], 'n4': nodes_4_hourly.mem[n]} for n in xrange(len(nodes_1_hourly.capt))]
    chart_cpu_hourly = [{'date': nodes_1_hourly.capt[n], 'n1': nodes_1_hourly.cpu[n], 'n2': nodes_2_hourly.cpu[n], 'n3': nodes_3_hourly.cpu[n], 'n4': nodes_4_hourly.cpu[n]} for n in xrange(len(nodes_1_hourly.capt))]
    chart_net_hourly = [{'date': nodes_1_hourly.capt[n], 'n1': nodes_1_hourly.net[n], 'n2': nodes_2_hourly.net[n], 'n3': nodes_3_hourly.net[n], 'n4': nodes_4_hourly.net[n]} for n in xrange(len(nodes_1_hourly.capt))]
    chart_conn_hourly = [{'date': nodes_1_hourly.capt[n], 'n1': nodes_1_hourly.conn[n], 'n2': nodes_2_hourly.conn[n], 'n3': nodes_3_hourly.conn[n], 'n4': nodes_4_hourly.conn[n]} for n in xrange(len(nodes_1_hourly.capt))]
    chart_mem_daily = [{'date': nodes_1_daily.capt[n], 'n1': nodes_1_daily.mem[n], 'n2': nodes_2_daily.mem[n], 'n3': nodes_3_daily.mem[n], 'n4': nodes_4_daily.mem[n]} for n in xrange(len(nodes_1_daily.capt))]
    chart_cpu_daily = [{'date': nodes_1_daily.capt[n], 'n1': nodes_1_daily.cpu[n], 'n2': nodes_2_daily.cpu[n], 'n3': nodes_3_daily.cpu[n], 'n4': nodes_4_daily.cpu[n]} for n in xrange(len(nodes_1_daily.capt))]
    chart_net_daily = [{'date': nodes_1_daily.capt[n], 'n1': nodes_1_daily.net[n], 'n2': nodes_2_daily.net[n], 'n3': nodes_3_daily.net[n], 'n4': nodes_4_daily.net[n]} for n in xrange(len(nodes_1_daily.capt))]
    chart_conn_daily = [{'date': nodes_1_daily.capt[n], 'n1': nodes_1_daily.conn[n], 'n2': nodes_2_daily.conn[n], 'n3': nodes_3_daily.conn[n], 'n4': nodes_4_daily.conn[n]} for n in xrange(len(nodes_1_daily.capt))]
    
    return render_to_response('stat.html', locals(), context_instance = RequestContext(request))