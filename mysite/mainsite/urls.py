from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('photo/', views.photo, name="photo"),
    path('photo/<slug:slug>/', views.photo_post, name="photo_post"),
    path('video/', views.video, name="video"),
    path('writing/', views.writing, name="writing"),
    path('diary/', views.diary, name="diary"),
    path('about/', views.about, name="about")
]