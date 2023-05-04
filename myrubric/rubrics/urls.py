from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('classes/', views.classes, name='classes_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
     path('add_class/', views.add_class, name='add_class'),
    
]