from django.db import models

class Contact(models.Model):    
    name = models.CharField(max_length=100)    
    message = models.CharField(max_length=500)    
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.name
    
class Projects(models.Model):
    image = models.ImageField(upload_to='projects/images/')
    title = models.CharField(max_length=50)    
    description = models.CharField(max_length=500)    
    link_to_code = models.URLField(blank=True)
    link_to_live_app = models.URLField(blank=True) 

    def __str__(self):
        return self.title

