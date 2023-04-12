from django.contrib import admin
from .models import Profile,Post,PostLike,FollowersCount

# Register your models here.

admin.site.register([Profile,Post,PostLike,FollowersCount])
