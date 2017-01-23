from django.contrib.auth.models import User
from django.db import models



# Create your models here.
class Book(models.Model):
    name = models.CharField( max_length=50 )
    author = models.CharField( max_length = 30 )
    genre = models.CharField( max_length = 30 )
    desc = models.CharField( max_length=2000, null=True  )
    imageUrl = models.CharField( max_length=100, null=True )
    orders = models.ManyToManyField( User )
    
    def __str__(self):
        return "Name = %s, Author = %s, Genre = %s" % (self.name, self.author, self.genre) 


