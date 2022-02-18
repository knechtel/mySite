import json
from django.core import serializers
from cadastro.models import Client
from django.http import HttpResponse


def index(request):
    clients = Client.objects.all()
    clients_list = serializers.serialize('json', clients)
    return HttpResponse(clients_list, content_type="text/json-comment-filtered")
