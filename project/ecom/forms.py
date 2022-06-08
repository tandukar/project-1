
from django import forms
from .models import Post 
from django.contrib.auth.forms import UserCreationForm


choices = []


class PostForm(forms.ModelForm):
    class Meta:
        model = Post # the database they belong to is Post
        fields = ('title','Seller', 'body', 'price', 'pack_img')

        widgets = {
            'title': forms.TextInput( attrs={'class': 'form-control'}),
            
            'Seller': forms.Select(choices = choices,attrs={'class': 'form-control'}),
            
            'price': forms.NumberInput( attrs={'class': 'form-control'}),
            'body': forms.Textarea( attrs={'class': 'form-control'}),
            
         
            # The widget handles the rendering of the HTML
            

        }

