from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.movies, name='movies'),
    path('file/', views.save_as, name='save_as'),

]