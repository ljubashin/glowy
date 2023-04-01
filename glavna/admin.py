from django.contrib import admin

# Register your models here.

from glavna.models import Video, Category

class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Video,VideoAdmin)
admin.site.register(Category)
