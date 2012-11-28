from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from center.models import Statistic, Node
from datetime import *

class Stat:
    def __init__(self, node_name, period):
        node_name = node_name.replace(' ', '_')
        start_time = datetime.now() - timedelta(hours = period, minutes = 1)
        stats = Statistic.objects.filter(node__name = node_name).filter(date__gt = start_time)
        self.name = node_name
        self.mem = [node.mem_load for node in stats]
        self.cpu = [node.cpu_load for node in stats]
        self.net = [node.net_load for node in stats]
        self.conn = [node.tcp_conn for node in stats]
        self.capt = [(node.date.year, node.date.month - 1, node.date.day, node.date.hour, node.date.minute) for node in stats]

@login_required
def stat(request):
    chart_hourly = list()
    chart_daily = list()
    nodes = [{'name': node.name.replace('_', ' '), 'color': node.color} for node in Node.objects.filter(is_active = True)]
    nodes_hourly = [Stat(node['name'], 1) for node in nodes]
    nodes_daily = [Stat(node['name'], 24) for node in nodes]

    for i in xrange(12):
        node_list = []
        for node in nodes_hourly:
            node_list.append({'name': node.name, 'mem': node.mem[i], 'cpu': node.cpu[i], 'net': node.net[i], 'conn': node.conn[i]})
        chart_hourly.append({'date': nodes_hourly[0].capt[i], 'nodes': node_list})
    for i in xrange(288):
        node_list = []
        for node in nodes_daily:
            node_list.append({'name': node.name, 'mem': node.mem[i], 'cpu': node.cpu[i], 'net': node.net[i], 'conn': node.conn[i]})
        chart_daily.append({'date': nodes_daily[0].capt[i], 'nodes': node_list})

    return render_to_response('stat.html', locals(), context_instance = RequestContext(request))
