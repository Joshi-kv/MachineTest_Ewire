from django.shortcuts import redirect, render
from . models import Profile,Post,PostLike
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='user:login')
def index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    posts = Post.objects.all()
    context = {
        'user_profile' : user_profile,
        'posts' : posts,
    }
    return render(request,'index.html',context)


#account settings
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


#post upload
def upload(request):
    if request.method == 'POST' :
        user = request.user.username
        image = request.FILES.get('post_image')
        title = request.POST['title']
        tag_string = request.POST['tag']
        description = request.POST['description']
        
        # split the tag string by comma and space, and remove any empty tags
        tags = [tag.strip() for tag_string in tag_string.split(',') for tag in tag_string.split() if tag]  
        tag_str = '#' + '#'.join(tags)  # join the tags with "#" symbol before each tag # join the list of tags into a comma-separated string with "#" in front of each tag
        new_post = Post.objects.create(
            user = user,
            post_image = image,
            title = title,
            tag = tag_str,
            description = description
            )
        print(tag_str)
        print(tags)
        new_post.save()
    return redirect('home:index')

def delete_post(request,post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('home:index',)

def like_post(request):
    
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = PostLike.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = PostLike.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.post_like = post.post_like+1
        post.save()
        return redirect('home:index')
    else:
        like_filter.delete()
        post.post_like = post.post_like-1
        post.save()
        return redirect('home:index')
    
def profile(request,pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_post = Post.objects.filter(user=pk)
    post_length = len(user_post)
    context = {
        'user_object' : user_object,
        'user_profile' : user_profile,
        'user_post' : user_post,
        'post_length' : post_length,
    }
    return render(request,'profile.html',context)