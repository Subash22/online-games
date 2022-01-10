from django.contrib import admin

from main.models import BookingModel, BroadcastModel, CategoryModel

# Register your models here.

admin.site.register(CategoryModel)
admin.site.register(BroadcastModel)
admin.site.register(BookingModel)