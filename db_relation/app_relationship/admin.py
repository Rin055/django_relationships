from django.contrib import admin
from .models import Profile, Address, Department, Employee, Course, Student

models = [Profile, Address, Department, Employee, Course, Student]

admin.site.register(models)
