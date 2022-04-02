from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Image, Profile
from .forms import NewImageForm
from django.contrib.auth.decorators import login_required
from .email import send_welcome_email

# Create your views here.
def index(request):

    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def timeline(request):
    photos = Image.objects.all()

    return render(request, 'instagram/timeline.html',{"photos":photos})

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


def profile(request):
    current_user = request.user
    images = Image.objects.filter(profile_id = current_user)

    return render(request, 'profile.html', {"images":images})
