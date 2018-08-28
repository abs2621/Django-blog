from django.contrib import admin
from .models import Post # imports our class from a different from model

admin.site.register(Post)
