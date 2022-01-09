from django.urls import path
from . import views



urlpatterns =[
    path('', views.register_user , name='register'),
    path('profile-page/', views.user_profile)
]