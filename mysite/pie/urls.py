from . import views
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    #path('', views.pie, name='pie'),

    path('', views.login.as_view(), name="login"),

#    path('pie-chart', views.pie, name='pie'),

]



