from django.urls import path
from . import views

app_name = 'extratest'

urlpatterns = [
    path('', views.index, name='index'),
    path('examples/', views.examples, name='examples'),
    path('input_number/', views.input_number, name='input_number'),
] 