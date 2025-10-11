from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    class_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.class_name})"


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    grade = models.IntegerField()

    def __str__(self):
        return f"{self.student} - {self.subject}: {self.grade}"
