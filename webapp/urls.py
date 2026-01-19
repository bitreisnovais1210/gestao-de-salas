from django.urls import path
from . import views

app_name = 'webapp'

urlpatterns = [
    path('', views.bem_vindo, name='bem_vindo'),
]
