from django.contrib import admin
from .models import Video, Comments

class VideoInLine(admin.StackedInline):
    model = Comments
    extra = 2

class VideoAdmin(admin.ModelAdmin):
    inlines = [VideoInLine]
    list_filter = ["Video_date"]

admin.site.register(Video, VideoAdmin)







# Register your models here.
