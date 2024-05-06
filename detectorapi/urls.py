from django.urls import path
from . import views


urlpatterns = [
  path('home/', views.index, name='index'),
  path('detector/', views.detector, name="detector"),
  path('contact/', views.contact, name="contact"),
  # api
  path('predict/', views.predict, name="predict"),
]