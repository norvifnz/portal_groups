from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student, Subject, Grade

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'class_name')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'grade', 'date')
    list_filter = ('subject', 'date')
