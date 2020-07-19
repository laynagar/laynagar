from django.contrib import admin
from .models import PictureCategoryModel, PictureModel

admin.site.register(PictureModel)
admin.site.register(PictureCategoryModel)