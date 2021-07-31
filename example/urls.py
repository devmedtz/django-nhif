from django.urls import path

from .import views

app_name = 'example'

urlpatterns = [
    path('token/', views.client_verification, name='client_verification')
]