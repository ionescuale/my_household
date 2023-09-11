from django.urls import path

from userextend import views

urlpattrens =[
    path('create_user/', views.UserCreateView.as_view(), name='create-user'),
]