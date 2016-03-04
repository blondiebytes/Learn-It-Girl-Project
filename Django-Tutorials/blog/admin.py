from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post) # Register your models here.
admin.site.register(Comment)
