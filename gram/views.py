from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Comment, Image,Like, Profile
from .forms import CommentForm, NewImageForm, UpdateProfileForm, RegistrationForm
from django.contrib.auth.decorators import login_required
from .email import send_welcome_email

# Create your views here.
def index(request):

    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def timeline(request):
    photos = Image.objects.all()

    return render(request, 'instagram/timeline.html',{"photos":photos})

def register(request):
    form = RegistrationForm()
    current_user = request.user
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('timeline')

    return render(request, 'registration/register.html', {"form":form, "user":current_user})

@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        name = request.GET.get("image")
        searched_images = Image.search_by_name(name)
        message = f"{name}"

        return render(request, 'instagram/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'instagram/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def search_profile(request):

    if 'profile' in request.GET and request.GET["profile"]:
        user = request.GET.get("profile")
        searched_user = Profile.search_by_user(user)
        message = f"{user}"

        return render(request, 'instagram/search_user.html',{"message":message,"user": searched_user})

    else:
        message = "You have not searched for any user."
        return render(request, 'instagram/search_user.html',{"message":message})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user
            image.save()
        return redirect('profile')

    else:
        form = NewImageForm()
    return render(request, 'instagram/new_image.html', {"form": form})

@login_required(login_url='/accounts/login/')
def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except Image.DoesNotExist:
        raise Http404()

    return render(request,"instagram/image.html", {"image":image})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    images = Image.objects.filter(profile_id = current_user)
    profile = Profile.objects.filter(user_id = current_user)

    return render(request, 'profile.html', {"images":images, "profile":profile})

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile')

    else:
        form = UpdateProfileForm()
    return render(request, 'update_profile.html', {"form": form})


@login_required(login_url='/accounts/login/')
def write_comment(request):
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.save()
        return redirect('timeline')

    else:
        form = CommentForm()
    return render(request, 'instagram/write_comment.html', {"form": form})

@login_required(login_url='/accounts/login/')
def comment(request):
    comments = Comment.objects.all()

    return render(request, 'instagram/comments.html',{"comments":comments})

@login_required(login_url='/accounts/login/')
def like(request):
    current_user = request.user
    if request.method == "POST":
        image_id = request.POST.get('image_id')
        image = Image.objects.get(id=image_id)

        if current_user in image.likes.all():
            image.likes.remove(current_user)
        else:
            image.likes.add(current_user)
    return redirect('timeline')
    
    

