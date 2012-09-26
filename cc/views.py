from django.shortcuts import render_to_response
from django.template import RequestContext
from cc.models import Statistic, ProxyServer
from datetime import *

def statistic(node, period):
    start_time = datetime.now() - timedelta(hours=period)
    stats = Statistic.objects.filter(node=node).filter(date__gt=start_time)
    mem = [node.mem_load for node in stats]
    cpu = [node.cpu_load for node in stats]
    net = [node.net_load for node in stats]
    conn = [node.tcp_conn for node in stats]
    captions = [(node.date.year, node.date.month - 1, node.date.day, node.date.hour, node.date.minute, node.date.second) for node in stats]
    return {'mem': mem, 'cpu': cpu, 'net': net, 'conn': conn, 'captions': captions}

def startpage(request):
    return render_to_response('startpage.html', locals(), context_instance = RequestContext(request))

def stat(request):
    nodes_1482_hourly = statistic('Node 1482', 1)
    nodes_1482_daily = statistic('Node 1482', 24)
    nodes_1483_hourly = statistic('Node 1483', 1)
    nodes_1483_daily = statistic('Node 1483', 24)
    nodes_1484_hourly = statistic('Node 1484', 1)
    nodes_1484_daily = statistic('Node 1484', 24)

    chart_mem_hourly = [{'date': nodes_1482_hourly['captions'][n], 'n1482': nodes_1482_hourly['mem'][n], 'n1483': nodes_1483_hourly['mem'][n], 'n1484': nodes_1484_hourly['mem'][n]} for n in xrange(len(nodes_1482_hourly['captions']))]
    chart_cpu_hourly = [{'date': nodes_1482_hourly['captions'][n], 'n1482': nodes_1482_hourly['cpu'][n], 'n1483': nodes_1483_hourly['cpu'][n], 'n1484': nodes_1484_hourly['cpu'][n]} for n in xrange(len(nodes_1482_hourly['captions']))]
    chart_net_hourly = [{'date': nodes_1482_hourly['captions'][n], 'n1482': nodes_1482_hourly['net'][n], 'n1483': nodes_1483_hourly['net'][n], 'n1484': nodes_1484_hourly['net'][n]} for n in xrange(len(nodes_1482_hourly['captions']))]
    chart_conn_hourly = [{'date': nodes_1482_hourly['captions'][n], 'n1482': nodes_1482_hourly['conn'][n], 'n1483': nodes_1483_hourly['conn'][n], 'n1484': nodes_1484_hourly['conn'][n]} for n in xrange(len(nodes_1482_hourly['captions']))]
    chart_mem_daily = [{'date': nodes_1482_daily['captions'][n], 'n1482': nodes_1482_daily['mem'][n], 'n1483': nodes_1483_daily['mem'][n], 'n1484': nodes_1484_daily['mem'][n]} for n in xrange(len(nodes_1482_daily['captions']))]
    chart_cpu_daily = [{'date': nodes_1482_daily['captions'][n], 'n1482': nodes_1482_daily['cpu'][n], 'n1483': nodes_1483_daily['cpu'][n], 'n1484': nodes_1484_daily['cpu'][n]} for n in xrange(len(nodes_1482_daily['captions']))]
    chart_net_daily = [{'date': nodes_1482_daily['captions'][n], 'n1482': nodes_1482_daily['net'][n], 'n1483': nodes_1483_daily['net'][n], 'n1484': nodes_1484_daily['net'][n]} for n in xrange(len(nodes_1482_daily['captions']))]
    chart_conn_daily = [{'date': nodes_1482_daily['captions'][n], 'n1482': nodes_1482_daily['conn'][n], 'n1483': nodes_1483_daily['conn'][n], 'n1484': nodes_1484_daily['conn'][n]} for n in xrange(len(nodes_1482_daily['captions']))]
    
    return render_to_response('stat.html', locals(), context_instance = RequestContext(request))