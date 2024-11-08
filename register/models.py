from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length= 200)
    last_name = models.CharField(max_length= 200)
    email = models.EmailField()
    profile_photo = models.ImageField(null= True, blank = True, upload_to = 'image/')

    class Meta:
        db_table = 'auth_user'
        swappable = 'AUTH_USER_MODEL'
