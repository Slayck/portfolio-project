from django.db import models
from datetime import datetime

class Blog(models.Model):
    image = models.ImageField(upload_to="images/", default='images/FEgif2.gif')
    user = models.CharField(max_length=50)
    blogTitle = models.CharField(max_length=200)
    blogNote = models.TextField()
    pubDate = models.DateTimeField(default=datetime.now())
    enabled = models.BooleanField()

    def __str__(self):
        return self.blogTitle


    def summary(self):
        blogSummary = self.blogNote[:100] + "..."
        return blogSummary

    def prettyPubDate(self):
        prettyDate = self.pubDate.strftime('%b %e %Y')
        return prettyDate
