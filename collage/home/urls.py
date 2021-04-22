from django.urls import path
from home import views
from home.views import HomeList

urlpatterns = [
    path('homeList/',views.HomeList,name='homeList'),
]