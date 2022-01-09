from django.forms import ModelForm
from .models import Posts


class CreatePostForm(ModelForm):

    class Meta:
        model = Posts
        fields = ['head','content', 'post_img']