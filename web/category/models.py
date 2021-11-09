from django.db import models
from django.db.models.deletion import CASCADE
import uuid

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(null=False,unique=True,default=uuid.uuid1)

    def __str__(self):
        return self.name 

