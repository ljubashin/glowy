from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("",views.homepageView.as_view(),name="home"),
    path("watch/<slug:slug>", views.videopage.as_view(), name="video"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
