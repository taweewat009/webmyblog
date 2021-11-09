from django.db import models
from django.db.models.deletion import CASCADE
from category.models import Category
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
import uuid

# Create your models here.
class Blogs(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    content = RichTextUploadingField(verbose_name='content')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    writer = models.CharField(max_length=255)
    views = models.IntegerField(default=0)
    images = models.ImageField(upload_to="blogImages",blank=True)
    create = models.DateTimeField(auto_now_add=True)
    grade = models.CharField(max_length=50)


    def get_url(self):
        return reverse('blogdetail', args=[self.category.slug,self.slug])
    
    def __str__(self):
        return self.name 


class PhotoAlbum(models.Model):
    picture = models.ImageField(upload_to="pictures",blank=True)
    
    