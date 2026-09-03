from django.contrib import path
from . import views

app_name = 'App01'

urlpatterns = [
    path('/v1', views.index, name= 'App01v1'),
    path('/v2', views.index, name= 'App01v2')
]