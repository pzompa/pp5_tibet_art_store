from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_us, name='contact_us'),
    path('contact-us/', views.contact_view, name='contact_view'),
    path('newsletter/', views.newsletter, name='newsletter')
]
