from django.contrib import admin

from blog.models import Post, Category

admin.site.register(Post)
admin.site.register(Category)
