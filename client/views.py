from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

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
	return render_to_response('room/dashboard.html', locals(), context_instance = RequestContext(request))

@login_required
def domains(request):
	return render_to_response('room/domains.html', locals(), context_instance = RequestContext(request))

@login_required
def support(request):
	return render_to_response('room/support.html', locals(), context_instance = RequestContext(request))
