from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class homepageView(TemplateView):
    template_name = "glavna/index.html"