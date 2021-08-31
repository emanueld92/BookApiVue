from django.db import models
from django.conf import settings
# Create your models here.
class Book(models.Model):
    def path_to_book(instance, filename):
        return f'book/{instance.id}/{filename}'
    
    title=models.CharField('Tile', max_length=50)
    decription=models.CharField("Description", max_length=150)
    year=models.DateTimeField("Year", auto_now=False)
    front_page=models.ImageField("Front Page", upload_to=path_to_book, height_field=None, width_field=None, max_length=None)
