from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.

class Category(models.Model):
    caption=models.CharField(max_length=40)

    def __str__(self):
        return self.caption
    
class Platforms(models.Model):
    platform_name=models.CharField(max_length=40)

    def __str__(self):
            return self.platform_name
class Genre(models.Model):
    genre=models.CharField(max_length=40,null=True, blank=True)

    def __str__(self):
            return self.genre
class Studio(models.Model):
    studio=models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
            return self.studio
class Producer(models.Model):
    producer=models.CharField(max_length=40,null=True, blank=True)

    def __str__(self):
            return self.producer

class Igdb(models.Model):
    name = models.CharField(max_length=200)
    cover_url = models.ImageField(null=True)
    summary = models.TextField(null=True)
    rating = models.FloatField(null=True)
    release_date = models.DateField(null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True, blank=True)
    platforms = models.ForeignKey(Platforms, on_delete=models.CASCADE, null=True, blank=True)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, null=True, blank=True)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Video(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='videos/thumbnails/', null=True)
    video = models.FileField(upload_to='videos/video/', validators=[FileExtensionValidator(allowed_extensions=["mp4", "mov"])])
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, related_name='user',on_delete=models.CASCADE, unique=False)    
    description=models.TextField(validators=[MinLengthValidator(10)], blank=True)
    category= models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    game = models.ForeignKey(Igdb, on_delete=models.CASCADE, null=True,blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Video, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class komentari(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="reviews")
    date = models.DateTimeField(auto_now=True)
    like = models.BooleanField()
