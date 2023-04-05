from django.urls import path
from . import views

urlpatterns = [
    path('home', views.dashboard, name='dashboard'),
    # Resource

    path('add-resource/', views.add_resource, name='add_resource'),
    path('resource/<int:pk>/', views.resource_detail, name='resource_detail'),
    path('resource/<int:pk>/edit/', views.edit_resource, name='edit_resource'),
    path('resource/<int:pk>/review/', views.review_resource, name='review_resource'),
    path('resource/<int:pk>/delete/', views.delete_resource, name='delete_resource'),
    path('resource/<int:resource_id>/add_review/', views.add_review, name='add_review'),
    path('resource_list/', views.resource_list, name='resource_list'),
    path('my_files/', views.my_files, name='my_files'),



]
