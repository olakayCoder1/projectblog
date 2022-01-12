from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.
class Posts(models.Model):
    head = models.CharField(max_length=50 , null=True , blank=True)
    content = models.TextField(max_length=10000)
    post_img = models.ImageField(null=True, blank=True ,upload_to="images/")
    date = models.DateTimeField(auto_now_add=True, null=True)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
