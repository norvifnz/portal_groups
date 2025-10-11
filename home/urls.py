from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('hub/', views.hub_page, name='hub'),
]
