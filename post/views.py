from django.shortcuts import render, redirect
from post.models import Posts
from django.contrib.auth.models import User
from post.forms import CreatePostForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required
# Create your views here.


def post_page(request):
    all_list = Posts.objects.all().order_by('date')[::-1]
    m = Paginator(all_list, 5)
    page = request.GET.get('page')
    try:
        me = m.page(page)
    except PageNotAnInteger:
# If page is not an integer, deliver first page.
        me = m.page(1)
    except EmptyPage:
# If page is out of range (e.g. 9999), deliver last page of results.
        me = m.page(m.num_pages)
    return render(request, 'post/posts.html', {'m': me})

@login_required
def add_post(request): 
    name = User.objects.get(id= request.user.id)
    head = request.POST.get('title')
    content = request.POST.get('content')
    img = request.POST.get('post_img')
    print(img)
    if request.method == 'POST':
        name.posts_set.create(head=head, content=content , post_img=img ).save()
        return redirect('posts')
    else:
        form =  CreatePostForm()
    return render(request, 'post/add_post.html', {'form': form })


def post_view(request, id):
    post= Posts.objects.get(id=id)
    return render(request, 'post/view-post.html', {'post': post })



    