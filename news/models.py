# shop/models.py

from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    publication_date = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title}, {self.publication_date}"

