from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(
            'auth.User',
            on_delete=models.CASCADE,
    )
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()

