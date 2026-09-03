from django.urls import path
from . import views

app_name = 'App01'

urlpatterns = [
    path('/v1', views.vista1_app1, name= 'App01v1'),
    path('/v2', views.vista1_app1, name= 'App01v2')
]