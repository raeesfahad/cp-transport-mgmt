from django.contrib import admin
from .models import *
from unfold.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group


from unfold.admin import ModelAdmin


admin.site.unregister(Group)



@admin.register(Bus)
class CustomAdminClass(ModelAdmin):
    pass

@admin.register(Route)
class CustomAdminClass(ModelAdmin):
    pass

@admin.register(Pass)
class CustomAdminClass(ModelAdmin):
    pass

@admin.register(PassValidation)
class CustomAdminClass(ModelAdmin):
    pass

@admin.register(Student)
class CustomAdminClass(ModelAdmin):
    pass

@admin.register(Schedule)
class CustomAdminClass(ModelAdmin):
    pass