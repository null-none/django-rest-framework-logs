from django.db import models


class Logger(models.Model):
    params = models.TextField()
    method_class = models.TextField()
    query = models.TextField()
    result = models.TextField()
    status = models.CharField(max_length=255)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.text
