from django.urls import path

from userextend import views

urlpatterns =[
    path('pages_register/', views.UserCreateView.as_view(), name='pages-register'),
    path('users_profile/<int:pk>/', views.UserDetailedView.as_view(), name='users-profile'),
]