from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects_list, name='projects'),
    path('contact/', views.contact, name='contact'),
    #path('', views.home, name='home'),
]