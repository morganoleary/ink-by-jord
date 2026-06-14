from django.db import models

# Create your models here.

class TattooImage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='tattoos/')
    category = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or "Tattoo Image"