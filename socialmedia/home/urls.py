from django.urls import path
from . import views


app_name = 'home'

urlpatterns = [
    path('',views.index,name='index'),
    path('settings/',views.settings,name='settings'),
    path('upload/',views.upload,name='upload'),
]
