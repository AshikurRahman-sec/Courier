from django.urls import path,include
from .views import *


urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('signup/',Signup.as_view(),name="signup"),
    path('logout/',Logout.as_view(),name='logout'),
    path('login/',LoginView.as_view(),name='login'),
    path('create-order/', create_order, name='create-order'),
    path('order-list/', OrderList.as_view(), name='orderlist'),
] 