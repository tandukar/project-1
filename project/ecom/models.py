from django.db import models
from django.forms import Textarea
from django.contrib.auth.models import User


from django.urls import reverse 

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255) 
    body =models.TextField(null = True, blank=True)
    price = models.IntegerField(default='',null=False)  
    Seller=models.ForeignKey(User, on_delete=models.CASCADE)
    pack_img = models.ImageField(null = True, blank=True, upload_to="pacImages/")

    
    def __str__(self):
        return self.title 


    def get_absolute_url(self):
        return reverse('products')
    
 