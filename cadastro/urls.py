from django.urls import path
from django.urls import include, path
from . import views
from django.contrib import admin
urlpatterns = [
    path('', views.index, name='index'),
    path('getAllClient', views.client, name='home'),

]

