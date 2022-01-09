"""projectblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views  as auth_view
from post import views as post_views
from users import views as users_views
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'), name='home'),
    path('register/',  users_views.register_user , name='register'),
    path('login', users_views.login, name='signin'),
   
    path('logout', auth_view.LogoutView.as_view(template_name='users/signout.html'), name='logout'),
    path('posts', post_views.post_page , name='posts') ,
    path('create-post/', post_views.add_post , name='create-post'),
    path('post/<str:id>', post_views.post_view , name='view-post'),
    path('profile-page/<str:id>', users_views.user_profile, name='profile-page')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)