from django.urls import path

from . import views

app_name = 'sugestions'
urlpatterns = [
    path('', views.contact, name='index'),
    #path('contact/',views.contact, name='contact'),
    #path('success/',views.successView, name='success'),
    ## ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
    ## ex: /polls/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    ## ex: /polls/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]
