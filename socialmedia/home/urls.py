from django.urls import path
from . import views


app_name = 'home'

urlpatterns = [
    path('',views.index,name='index'),
    path('settings/',views.settings,name='settings'),
    path('upload/',views.upload,name='upload'),
    path('delete/<int:post_id>/',views.delete_post,name='delete'),
    path('like/',views.like_post,name='like'),
    path('profile/<str:pk>/',views.profile,name='profile'),
    path('follow/',views.follow,name='follow'),
]
