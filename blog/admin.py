from django.contrib import admin
from .models import Post #from the Post class defined in models.py in the blog directory

admin.site.register(Post)#to make post available on the admin page, need to register