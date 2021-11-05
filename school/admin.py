from django.contrib import admin

from .models import Work, Schedule, CheckList

# Register your models here.

admin.site.register(Work)
admin.site.register(Schedule)
admin.site.register(CheckList)
