from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('gallery/', views.gallery, name='gallery'),
]
