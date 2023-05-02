from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views import View
from .models import Video, User
from django.http import HttpResponseRedirect
from .forms import komentariform, videoupload
from django.urls import reverse

# Create your views here.

class homepageView(ListView):
    template_name = "glavna/index.html"
    model = Video
    ordering = ['-date']
    context_object_name = "videos"

    def get_queryset(self):
        querySet = super().get_queryset()
        data = querySet[:20]
        return data

def uploadpage(request):
    if request.method == "POST":
        form = videoupload(request.POST or None, request.FILES or None)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            return redirect("home")
    else:
        form = videoupload()
    
    return render(request, "glavna/upload.html", {"form": form})

class videopage(DetailView):
    def get(self,request, slug):
        video = Video.objects.get(slug=slug)
        context = {
            "video" : video,
            "review_form": komentariform(),
            "reviews": video.reviews.all(),
        }
        return render(request,"glavna/videostranica.html",context)

    def post(self,request, slug):
        review_form = komentariform(request.POST)
        video = Video.objects.get(slug=slug)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.video = video
            review.user_name = request.user
            review.save()
            return HttpResponseRedirect(reverse("video",args=[slug]))
        context = {
            "video" : video,
            "review_form": komentariform(),
            "reviews": video.reviews.all(),
        }   
        return render(request,"glavna/videostranica.html",context)