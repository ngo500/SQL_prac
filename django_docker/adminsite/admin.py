from django.contrib import admin
from .models import Course, Instructor, Lesson

class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']

admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor)
