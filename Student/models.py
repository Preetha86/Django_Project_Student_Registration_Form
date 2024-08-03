from django.db import models

# Create your models here.

'''class Stud(models.Model):
    Name = models.CharField(max_length=40)
    Email = models.CharField(max_length=100)
    Age = models.IntegerField()
    Sex = models.CharField(max_length=10)
    Contact = models.IntegerField()
    Score = models.FloatField()
    Course = models.CharField(max_length=40)'''

"""class Stud1(models.Model):
    Name = models.CharField(max_length=40)
    Email = models.CharField(max_length=100)
    Age = models.IntegerField()
    Sex = models.CharField(max_length=10)
    Contact = models.IntegerField()
    Score = models.FloatField()
    Course = models.CharField(max_length=40)"""

class Stud2(models.Model):
    Name = models.CharField(max_length=40)
    Email = models.CharField(max_length=100)
    Age = models.IntegerField()
    Sex = models.CharField(max_length=10)
    Contact = models.IntegerField()
    Score = models.FloatField()
    Course = models.CharField(max_length=40)