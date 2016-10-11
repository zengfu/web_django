from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ic(models.Model):
    mypn=models.CharField(max_length=30)
    value = models.CharField(max_length=30,null=True)
    type = models.CharField(max_length=30,null=True)
    description = models.TextField(max_length=100,null=True)
    venderpn = models.CharField(max_length=30,null=True)
    datasheet =models.FileField(max_length=100,null=True,upload_to='datasheet/')
    refdesign=models.URLField()
    refcode=models.FileField(max_length=100,upload_to='refcode/')
    refsch = models.FileField(max_length=100,upload_to='resch/')
    state=models.NullBooleanField()

    def __str__(self):
        return self.mypn