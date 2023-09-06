from django.db import models

# Create your models here


class ShortUrl(models.Model):
    url = models.URLField()
    short_url = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short_url
