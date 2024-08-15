from django.contrib import admin
from .models import Student

class Studentadmin(admin.ModelAdmin):
    list_display=['name', 'address', 'course', 'passed_by']
admin.site.register(Student)