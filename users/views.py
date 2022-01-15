from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.forms import RegisterUser




def register_user(request):

    if request.method == 'POST':
        print(request.POST)

        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.Error(request, 'Username Already Exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.Info(request, 'Email Already In Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password2)
                user.save()
                return redirect('signin')
        else:
            messages.Info(request, 'Password does not matched')
            return render(request, 'users/register.html')

    else:
        return render(request, 'users/register.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('posts')
        else:
            messages.Error(request, "You don't have account with use please sign up first")
            return redirect('signin')



    return render(request, 'users/signin.html')

@login_required
def user_profile(request, id):
    name = User.objects.get(id=id)
    user_posts = name.posts_set.all()
    return render(request, 'users/profile.html', {'user_post': user_posts , 'name': name})
