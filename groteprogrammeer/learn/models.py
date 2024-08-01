from django.db import models


# Create your models here.
class Lesson(models.Model):
    title = models.CharField(max_length=128)
    path = models.CharField(max_length=64)
    content = models.TextField()

    def __str__(self):
        return "%s: %s" % (self.path, self.title)
