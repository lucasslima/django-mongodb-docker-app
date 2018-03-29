from django.urls import path

from . import views

app_name = 'sugestions'
urlpatterns = [
    path('', views.contact, name='index'),
]
