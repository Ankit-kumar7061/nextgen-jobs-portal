from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('hyd/', views.hydjobs_view),
    path('blore/', views.blorejobs_view),
    path('chennai/', views.chennaijobs_view),
    path('pune/', views.punejobs_view),
]