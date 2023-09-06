from django.contrib import admin
from .models import ShortUrl
# Register your models here.


@admin.register(ShortUrl)
class ShortUrlAdmin(admin.ModelAdmin):
    list_display = ('short_url', 'url', 'created_at')
    list_display_links = ('short_url', 'url')
    search_fields = ('url',)
    list_per_page = 20

