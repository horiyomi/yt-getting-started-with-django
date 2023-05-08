from django.db import models


class News(models.Model):
    headline = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.headline
