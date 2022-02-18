import json
from django.core import serializers
from cadastro.models import Client
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    # clients = Client.objects.all()
    # serialized_obj = serializers.serialize('json', clients)
    # return HttpResponse(serialized_obj, content_type="text/json-comment-filtered")
    return render(request, 'cadastro/index.html')
