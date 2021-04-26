from django.db import models

class Course(models.Model):
	name = models.CharField(max_length=20)

class Student(models.Model):
	name = models.CharField(max_length=20)
	age = models.IntegerField()
	email = models.EmailField()
	courses = models.ManyToManyField(Course)



