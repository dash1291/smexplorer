from django.db import models

class Directory(models.Model):
    path = models.TextField(primary_key=True)

class File(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField()
    path = models.ForeignKey(Directory)
    size = models.IntegerField()
    last_edited = models.DateTimeField()
    created = models.DateTimeField()

# Create your models here.
