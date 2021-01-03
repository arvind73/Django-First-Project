from django.urls import path
from second_app import views

urlpatterns = [  
    path('', views.help, name='help'),
    path('users', views.users,name='users'),
    path('home', views.home,name='home')
]