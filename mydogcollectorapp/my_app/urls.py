from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('about/', views.about, name='about'),
   path('mountains/', views.mountain_index, name='mountain-index'),
   path('mountains/<int:mountain_id>/', views.mountain_detail, name='mountain-detail'),
]