from django.urls import path
from home import views
from home.views import HomeList, ClassifyList, HomeDetails,getToken

urlpatterns = [
    path('homeList/',views.HomeList,name='homeList'),
    path('classifyList/',views.ClassifyList,name='classifyList'),
    path('homeDetails/',views.HomeDetails,name='homeDetails'),
    path('api/get_token/',views.getToken,name='get_token'),
]