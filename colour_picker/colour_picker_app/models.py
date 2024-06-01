from django.utils import timezone
from django.db import models

# Create your models here.
class Image_Upload(models.Model):
    date_uploaded = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="image_uploads")

class Colour_Store(models.Model):
    date_uploaded = models.DateTimeField(default=timezone.now)
    colour_value = models.CharField(max_length=30)
    type = models.CharField(max_length=30)