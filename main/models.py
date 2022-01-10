from django.db import models
from django.conf import settings


# Create your models here.
class CategoryModel(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class BroadcastModel(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True, blank=True)
    video_url = models.CharField(max_length=100, null=True, blank=True)
    date_publish = models.DateTimeField()
    date_created = models.DateField(auto_now_add=True)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class BookingModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    broadcast = models.ForeignKey(BroadcastModel, on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.broadcast.name
