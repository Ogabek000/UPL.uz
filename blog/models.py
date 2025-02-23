from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from config import settings


# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)


class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Article(models.Model):
    title = models.CharField(max_length=250, unique=True)
    info = models.TextField(blank=True)
    photo = models.ImageField(upload_to="articles/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def get_photo(self):
        try:
            return self.photo.url
        except:
            return "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMmyTPv4M5fFPvYLrMzMQcPD_VO34ByNjouQ&s"

    def get_absolute_url(self):
        return reverse("detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title


