from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('v1/', views.vista1_app1, name= 'app1v1'),
    path('v2/', views.vista2_app1, name= 'app1v2')
]