from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('business_query', views.business_query, name='business_query'),
    path('locations_query', views.locations_query, name='locations_query')
]
