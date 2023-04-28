from app1 import views
from django.urls import path

urlpatterns = [
    path('form/',views.django_forms,name='django_forms')
]