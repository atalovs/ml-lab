from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    youtube_url = models.URLField()

    def __str__(self):
        return self.title
