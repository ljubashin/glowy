from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views import View
from .models import Video

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
        }
        return render(request,"glavna/videostranica.html",context)