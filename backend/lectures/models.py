from django.db import models

class Lecture(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
