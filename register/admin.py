
# Register your models here.
from django.contrib import admin    #copied from wshop registration admin.py
from register.models import *

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)
