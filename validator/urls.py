from django.urls import path
from . import views

app_name = 'validator'

urlpatterns = [
    path('', views.validate, name='validate_page'),
    path('validate/', views.validate_number, name='submit_validate'),
]