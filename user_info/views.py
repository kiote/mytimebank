from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import UserInfo

def index(request):
    template = loader.get_template('user_info/index.html')
    context = RequestContext(request, {'users': UserInfo.objects.all()})
    return HttpResponse(template.render(context))
