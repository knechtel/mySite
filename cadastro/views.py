import json
from django.core import serializers
from cadastro.models import Client
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from cadastro.serializers import ClientSerializer
from rest_framework.renderers import JSONRenderer
def index(request):
    # clients = Client.objects.all()
    # serialized_obj = serializers.serialize('json', clients)
    # return HttpResponse(serialized_obj, content_type="text/json-comment-filtered")
    return render(request, 'cadastro/index.html')


def getAllClient(request):
    clients = Client.objects.all()
    clientSerializer = ClientSerializer(many=True)
    clientList = clientSerializer.to_representation(clients)
    renderer = JSONRenderer()
    return HttpResponse(renderer.render(clientList), content_type="text/json-comment-filtered")
