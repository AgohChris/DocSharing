from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_picture/', null=True, blank=True)
    profession = models.CharField(max_length=80)
    email = models.EmailField(max_length=255, unique=True)
    reset_code = models.CharField(max_length=4, blank=True, null=True)
    
    
    def __str__(self):
        return f"{self.user.username}, {self.profile_picture}, il est : {self.profession}"
    

class Document(models.Model):
    title =models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='documents/')
    cover_image = models.ImageField(upload_to='couvertur_image', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} {self.description}"
    