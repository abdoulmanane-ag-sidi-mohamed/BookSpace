from django.db import models

# Create your models here.
class Book(models.Model):  

    def __str__(self):
        return f"{self.title}({self.author_name})"

    title = models.CharField(max_length=100)    #titre du livre
    author_name = models.CharField(max_length=100) #nom de l'auteur
    genre = models.CharField(max_length=100) #genre du livre
    year_pub = models.IntegerField()               #année de publication du livre
    available = models.BooleanField(default=True)  #disponibilité du livre