from django.db import models

# Create your models here.


class Number_store(models.Model):
    num = models.IntegerField()
    userid = models.CharField(max_length=30)
    class Meta:
        db_table = 'Number_store'

class FileUpload(models.Model):
    file = models.FileField(upload_to="ExcelFiles")