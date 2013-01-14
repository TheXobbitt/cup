from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from django.contrib.auth.models import User
from center.models import Domain, Tariff, BlackList, SiteStatistic
from client.models import UserProfile

from datetime import datetime, timedelta
import socket

class Stat:
    def __init__(self, site_name, period):
        start_time = datetime.now() - timedelta(hours = period, minutes = 1)
        stats = SiteStatistic.objects.filter(site__name = site_name).filter(date__gt = start_time)
        site_info = [{'date': '%s.%s.%s.%s.%s' % (site.date.year, site.date.month - 1, site.date.day, site.date.hour, site.date.minute), 'error': site.error, 'access': site.access} for site in stats]
        site_date = ['%s.%s.%s.%s.%s' % (site.date.year, site.date.month - 1, site.date.day, site.date.hour, site.date.minute) for site in stats]
        site_date = [e for i,e in enumerate(site_date) if e not in site_date[:i]]
        site_info_tmp = []
        for date in site_date:
            error = 0
            access = 0
            for info in site_info:
                if info['date'] == date:
                    error += info['error']
                    access += info['access']
            site_info_tmp.append({'date': date, 'error': error, 'access': access})
        site_info = site_info_tmp
        capt_tmp = [info['date'].split('.') for info in site_info]
        capt = []
        for date in capt_tmp:
            capt.append([int(i) for i in date])
        self.name = site_name
        self.error = [info['error'] for info in site_info]
        self.access = [info['access'] for info in site_info]
        self.capt = [tuple(i) for i in capt]

def index(request):
    return render_to_response('general/index.html', locals(), context_instance = RequestContext(request))

def features(request):
    return render_to_response('general/features.html', locals(), context_instance = RequestContext(request))

def pricing(request):
    return render_to_response('general/pricing-tables.html', locals(), context_instance = RequestContext(request))

def elements(request):
    return render_to_response('general/elements.html', locals(), context_instance = RequestContext(request))

def contact(request):
    return render_to_response('general/contact-us.html', locals(), context_instance = RequestContext(request))

@login_required
def billing(request):
    return render_to_response('room/billing.html', locals(), context_instance = RequestContext(request))

@login_required
def dashboard(request):
    client = UserProfile.objects.get(user=request.user)
    domains = Domain.objects.filter(user=request.user).filter(is_active=True)
    site_stat = [Stat(domain.name, 1) for domain in domains]

    chart = []
    for i in xrange(12):
        site_list = []
        for site in site_stat:
            site_list.append({'name': site.name, 'error': site.error[i], 'access': site.access[i]})
        chart.append({'date': site_stat[0].capt[i], 'sites': site_list})

    black_ips = BlackList.objects.all()

    return render_to_response('room/dashboard.html', locals(), context_instance = RequestContext(request))

@login_required
def domains(request):
#    client = UserProfile.objects.get(user=request.user)
#    tariff_name = client.tariff
#    domains = client.domains.all()
#    tariff = Tariff.objects.get(name=tariff_name)
#    if tariff.waf == 'no':
#        tariff.waf = False
#    else:
#        tariff.waf = True
#    tariff_cache = {'1440': '1 day', '60': '1 hour', '10': '10 minutes'}
#    tariff_support = {'tick': 'Tickets', 'tel': 'Tickets, Telephone', 'adm': 'Tickets, Telephone, Admin'}
#    tariff = {'antidos': tariff.antidos, 'cache': tariff_cache[tariff.cache], 'compression': tariff.compression, 'waf': tariff.waf, 'monitoring': tariff.monitoring, 'geoban': tariff.geoban, 'support': tariff_support[tariff.support]}
#
    return render_to_response('room/domains.html', locals(), context_instance = RequestContext(request))

@login_required
def support(request):
    return render_to_response('room/support.html', locals(), context_instance = RequestContext(request))

@login_required
def add_new_site(request):
    tariffs = Tariff.objects.all()
    if request.method == 'POST':
        site = request.POST['site']
        tariff = request.POST['tariff']
        site_ip = [ip[4][0] for ip in socket.getaddrinfo(site, 80)]
        site_ip = ';'.join(site_ip)
        Domain.objects.create(user=request.user, name=site, ip=site_ip, is_active=True)
        return redirect('/dashboard/')

    return render_to_response('room/add_new_site.html', locals(), context_instance = RequestContext(request))
