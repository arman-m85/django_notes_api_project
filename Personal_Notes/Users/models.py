from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser


from Users.user_manager import CustomUserManager# Create your models here.

class user(AbstractUser):
    phone_number= models.CharField(max_length = 11,unique = True)
    username = models.CharField(max_length=150, null=True , blank= True,unique=False)

    USERNAME_FIELD = "phone_number"
    
    objects = CustomUserManager()
    
class Note(models.Model):
    owner = models.ForeignKey(user, on_delete=models.CASCADE,related_name="owner_note")
    title = models.CharField(max_length=255)
    data = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
    
    

