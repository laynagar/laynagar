from django.db import models
from PIL import Image


class PictureCategoryModel(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

# Category, Picture, Title, Date, 
import datetime

def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year

class PictureModel(models.Model):
    category = models.ForeignKey(PictureCategoryModel, on_delete=models.CASCADE, related_name='photos')
    title = models.CharField(max_length=50)
    year = models.IntegerField(('year'), choices=year_choices(), default=current_year)
    image = models.ImageField(upload_to=f'{category}')

    def __str__(self):
        return self.title+" ("+str(self.category.category)+")"