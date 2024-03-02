from django.urls import path, re_path

from blog import views

urlpatterns = [
    path('', views.index, kwargs=
    {'name': 'Daniel'}),
    path('about/', views.about, kwargs=
    {"name": "Daniel"})
]