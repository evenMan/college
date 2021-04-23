from django.urls import path
from home import views
from home.views import HomeList, ClassifyList, HomeDetails

urlpatterns = [
    path('homeList/',views.HomeList,name='homeList'),
    path('classifyList/',views.ClassifyList,name='classifyList'),
    path('homeDetails/',views.HomeDetails,name='homeDetails'),
]