from django.contrib import admin

# Register your models here.

from glavna.models import Video, Category, komentari, Igdb,Platforms,Genre,Studio, Producer

class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Video,VideoAdmin)
admin.site.register(Category)
admin.site.register(komentari)
admin.site.register(Igdb)
admin.site.register(Platforms)
admin.site.register(Genre)
admin.site.register(Studio)
admin.site.register(Producer)
