from django.urls import path
from home import views
from home.views import HomeList, ClassifyList, HomeDetails,getToken,get_code, decrypt

urlpatterns = [
    path('homeList/',views.HomeList,name='homeList'),
    path('classifyList/',views.ClassifyList,name='classifyList'),
    path('homeDetails/',views.HomeDetails,name='homeDetails'),
    path('api/code/',views.get_code,name='code'),
    path('api/get_token/',views.getToken,name='get_token'),
    path('api/register/',views.RegisterUsers,name='register'),
    path('api/decrypt/',views.decrypt,name='decrypt'),
    path('api/getUserInfo/',views.GetUserInfo,name='getUserInfo'),
]