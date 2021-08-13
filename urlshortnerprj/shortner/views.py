from django.shortcuts import render, redirect
import uuid
from .models import Urls
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def create(request):
    if request.method == "POST":
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Urls(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)


def search(request, pk):
    url_Details = Urls.objects.get(uuid=pk)
    return redirect('https://'+url_Details.link)
