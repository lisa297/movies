
from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, name='list'),
    #path('review/', views.review_create, name='review'),
    path('<slug:slug>/', views.movie_detail, name='detail'),
]