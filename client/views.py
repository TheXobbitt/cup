from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('index.html', locals(), context_instance = RequestContext(request))

def features(request):
    return render_to_response('features.html', locals(), context_instance = RequestContext(request))

def pricing(request):
    return render_to_response('pricing-tables.html', locals(), context_instance = RequestContext(request))

def elements(request):
    return render_to_response('elements.html', locals(), context_instance = RequestContext(request))

def contact(request):
    return render_to_response('contact-us.html', locals(), context_instance = RequestContext(request))
