from django.db import models

# Create your models here.
class PdfFile(models.Model):
    # desc = models.CharField(max_length=255)
    # qty = models.CharField(max_length=255)
    billfile = models.FileField(upload_to = 'bill/')
    uploading_date = models.DateTimeField(auto_now_add=True)
