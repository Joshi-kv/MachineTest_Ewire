from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_pic',default='blank-profile.png',blank=True,null=True)
    location = models.CharField(max_length=100,blank=True)
    
    def __str__(self):
        return f'{self.user.username}'
    
class Post(models.Model):
    user = models.CharField(max_length=100)
    title = models.CharField(max_length=300)
    post_image = models.ImageField(upload_to='post_image')
    description = models.TextField(blank=True)
    tag = models.CharField(max_length=500)
    post_date = models.DateTimeField(auto_now_add=True)
    post_like = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.title}'
    
    