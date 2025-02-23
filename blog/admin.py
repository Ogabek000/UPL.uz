from django.contrib import admin
from blog.models import Category, Article, CustomUser

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Article)