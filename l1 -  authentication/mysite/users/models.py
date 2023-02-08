from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class User_Detail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    email= models.EmailField(max_length=255, unique=True)
    username= models.CharField(max_length=255, unique=True)
    
    def __str__(self) -> str:
        return self.username
    
    
    