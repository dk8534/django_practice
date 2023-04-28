"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views as v1
# from app2 import views # this app2 views is override the first app views and through an error 
# for solution : use alias name concept
from app2 import views as v2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('testapp/',v1.display),
    path('datetime/',v1.getdatetime),
    path('dt/',v1.get_greeting_mesg),
    path('dt1/',v1.get_greeting_mesg),
    path('view2/',v2.app2_view),
    path('index/',v2.index_view),
    path('home/',v1.home_view),
]
