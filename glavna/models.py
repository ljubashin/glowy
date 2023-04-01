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

class Video(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='videos/thumbnails/', null=True)
    video = models.FileField(upload_to='videos/video/', validators=[FileExtensionValidator(allowed_extensions=["mp4", "mov"])])
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    user = models.OneToOneField(User, related_name='user',on_delete=models.CASCADE)    
    description=models.TextField(validators=[MinLengthValidator(10)])
    category= models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Video, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
