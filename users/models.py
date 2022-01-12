from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    profile_img = models.ImageField( upload_to='images/', default='default.jpg', null=True, blank=True)
    user_img_id = models.OneToOneField(User,null=True, on_delete=models.CASCADE)



   