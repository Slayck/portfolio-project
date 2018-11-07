from django.db import models
from datetime import datetime

class Blog(models.Model):
    image = models.ImageField(upload_to="images/", default='images/FEgif2.gif')
    user = models.CharField(max_length=50)
    blogNote = models.TextField()
    pubDate = models.DateTimeField(default=datetime.now())
    enabled = models.BooleanField()
