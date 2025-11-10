from django.db import models


class Profile(models.Model):
    user_name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.user_name} ({self.age}y)"

class Address(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city}, {self.country}"



class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.department.name})"



class Course(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.name} ({self.courses.count()} courses)"
