from django.urls import path
from . import views

urlpatterns = [
    path('', views.materials_list, name='materials_list'),
    path('add/', views.material_create, name='material_create'),
    path('<int:pk>/edit/', views.material_edit, name='material_edit'),
    path('<int:pk>/delete/', views.material_delete, name='material_delete'),
]
