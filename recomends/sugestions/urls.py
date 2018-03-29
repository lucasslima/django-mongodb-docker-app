from django.urls import path

from . import views

app_name = 'sugestions'
urlpatterns = [
    path('', views.sugestions, name='sugestions'),
    path('success/', views.successView, name='success')
]
