from django.urls import path
from . import views # import the views from the directory

urlpatterns = [
  path('', views.index, name='index'),
]