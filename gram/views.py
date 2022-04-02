from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Image
from .forms import NewImageForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):

    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def timeline(request):
    photos = Image.objects.all()

    return render(request, 'instagram/timeline.html',{"photos":photos})

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

    return render(request, 'profile.html')
