from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views import View
from .models import Video
from django.http import HttpResponseRedirect
from .forms import komentariform
from django.urls import reverse

# Create your views here.

class homepageView(ListView):
    template_name = "glavna/index.html"
    model = Video
    ordering = ['-date']
    context_object_name = "videos"

    def get_queryset(self):
        querySet = super().get_queryset()
        data = querySet[:4]
        return data

class videopage(View):
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