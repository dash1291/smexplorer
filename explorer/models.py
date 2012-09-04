from django.db import models

class Directory(models.Model):
    path = models.TextField(primary_key=True)
    
    def __unicode__(self):
        return self.path

    def __str__(self):
        return self.path


class File(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    path = models.ForeignKey(Directory)
    size = models.IntegerField()
    last_modified = models.DateTimeField()

    def get_full_path(self):
        return self.path.path + '/' + self.name
# Create your models here.
