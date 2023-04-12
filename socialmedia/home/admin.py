from django.contrib import admin
from .models import Profile,Post,PostLike

# Register your models here.

admin.site.register([Profile,Post,PostLike])
