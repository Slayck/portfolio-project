from django.db import models

class Blog(models.Model):
    user = models.CharField(max_length=50)
    blogNote = models.CharField(max_length=500)
    enabled = models.BooleanField()
