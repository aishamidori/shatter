from django.contrib import admin
from .models import Company, Comment, Tag_Type

# Register your models here.
admin.site.register(Company)
admin.site.register(Comment)
admin.site.register(Tag_Type)
