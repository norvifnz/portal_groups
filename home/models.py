from django.db import models

class GroupInfo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='group/', blank=True)

    def __str__(self):
        return self.title
