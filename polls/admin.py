from django.contrib import admin

from .models import Question
from .models import Client

admin.site.register(Question)

admin.site.register(Client)
