from django.db import models

class directory(models.Model):
    path = models.TextField()
    name = models.TextField()

class file(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField()
    path = models.ForeignKey(directory)
    size = models.IntegerField()
    last_edited = models.DateTimeField()
    created = models.DateTimeField()

# Create your models here.
