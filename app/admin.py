from django.contrib import admin

# Register your models here.
from .models import *

from django.contrib.auth.admin import UserAdmin
# class usermodel(UserAdmin):
#     list_display=['username','user_Type']

admin.site.register(Customeuser)
# admin.site.register(Cource)
admin.site.register(Sessionyear)
admin.site.register(Student)