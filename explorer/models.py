from django.db import models

class Directory(models.Model):
    path = models.TextField(primary_key=True)
    def __unicode__(self):
        return self.path


class File(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    path = models.ForeignKey(Directory)
    size = models.IntegerField()
    last_modified = models.DateTimeField()


# Create your models here.
