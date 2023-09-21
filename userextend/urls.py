from django.urls import path

from userextend import views
from .views import update_profile

urlpatterns =[
    path('pages_register/', update_profile, name='pages-register'),
    path('users_profile/<int:pk>/', views.UserDetailedView.as_view(), name='users-profile'),
]