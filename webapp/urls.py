from django.urls import path
from . import views

app_name = 'webapp'

urlpatterns = [
    path('', views.bem_vindo, name='bem_vindo'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('logout/', views.logout_view, name='logout'),
]
