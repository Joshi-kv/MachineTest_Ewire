from django.shortcuts import redirect, render
from . models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='user:login')
def index(request):
    return render(request,'index.html')

def settings(request):
    user_profile = Profile.objects.get(user=request.user)
    
    if request.method == 'POST':
        
        if request.FILES.get('image') == None:
            image = user_profile.profile_image
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profile_image = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profile_image = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        
        return redirect('home:settings')
    context = {
        'user_profile':user_profile
    }
    return render(request,'setting.html',context)