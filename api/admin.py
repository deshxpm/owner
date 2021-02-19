from django.contrib import admin

from .models import *


class TestAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')



admin.site.register(Test, TestAdmin)
