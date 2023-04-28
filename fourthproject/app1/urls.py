# from app1 import views   (we can use this also)
from . import views

from django.urls import path

urlpatterns=[
    path('',views.home_view),
    path('news/',views.news_view)
]