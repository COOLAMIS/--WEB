from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .forms import FileForm
from .models import File, Photo, Music, Video, update_filename


# Create your views here.
def main(request):
    return render(request, 'app_download/index.html', context={"title": "DownLoad"})



def upload(request):
    form = FileForm(instance=File())
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES, instance=File())
        if form.is_valid():
            form.save()
            return redirect(to="app_download:files")
    return render(request, 'app_download/upload.html', context={"title": "DownLoad", "form": form})

def files(request):
    files = File.objects.all()
    return render(request, 'app_download/files.html', context={"title": "DownLoad", "files": files})

def photo(request):
    photo = Photo.objects.all()
    return render(request, 'app_download/photo.html', context={"title": "DownLoad", "photo": photo})

def music(request):
    music = Music.objects.all()
    return render(request, 'app_download/music.html', context={"title": "DownLoad", "music": music})

def video(request):
    video = Video.objects.all()
    return render(request, 'app_download/video.html', context={"title": "DownLoad", "video": video})

def other(request):
    video = Video.objects.all()
    return render(request, 'app_download/other.html', context={"title": "DownLoad", "other": other})