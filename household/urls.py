from django.urls import path

from household import views

urlpatterns =[
    path('', views.index, name='index'),
    path('create_household/', views.HouseholdCreateView.as_view(), name='create-household'),
    path('list_household/', views.HouseholdListView.as_view(), name='list-household'),

]