from django.urls import path
from news_app import views

urlpatterns=[
    path('',views.home_view),
    path('aligarh/',views.aligarh_view),
    path('noida/',views.noida_view),
    path('delhi/',views.delhi_view)
]