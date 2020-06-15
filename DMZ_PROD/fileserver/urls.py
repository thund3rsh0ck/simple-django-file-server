from django.urls import path

from . import views

#This file adds our pages so that they can be viewed.
urlpatterns = [
    path('', views.index, name='index'),
    path('privatefilelist/', views.privatefilelist, name='privatefilelist'),
    path('publicfilelist/', views.publicfilelist, name='publicfilelist'),
]
