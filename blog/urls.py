from django.urls import path, re_path

from blog import views

urlpatterns = [
    path('', views.index, name="home",
         kwargs={'name': 'Daniel'}),
    path('about/', views.about, name="about",
         kwargs={"name": "Daniel"})
]