from django.db import models

class Contact(models.Model):    
    name = models.CharField(max_length=100)    
    message = models.CharField(max_length=500)    
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.name
