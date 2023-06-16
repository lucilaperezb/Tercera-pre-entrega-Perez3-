from django.db import models

class Class1(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()

class Class2(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()

class Class3(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
