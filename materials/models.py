from django.db import models
from django.contrib.auth.models import User

class Material(models.Model):
    TYPE_CHOICES = [
        ('file', 'Файл'),
        ('image', 'Зображення'),
        ('video', 'YouTube відео'),
        ('link', 'Посилання'),
    ]

    title = models.CharField(max_length=255, verbose_name="Назва")
    description = models.TextField(blank=True, verbose_name="Опис")
    material_type = models.CharField(max_length=10, choices=TYPE_CHOICES, verbose_name="Тип матеріалу")
    file = models.FileField(upload_to='materials/files/', blank=True, null=True)
    image = models.ImageField(upload_to='materials/images/', blank=True, null=True)
    link = models.URLField(blank=True, null=True, verbose_name="Посилання (YouTube або інше)")
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def youtube_embed(self):
        """Перетворює YouTube посилання у формат для вбудовування"""
        if self.link and 'youtube.com' in self.link:
            video_id = self.link.split('v=')[-1]
            return f"https://www.youtube.com/embed/{video_id}"
        elif self.link and 'youtu.be' in self.link:
            video_id = self.link.split('/')[-1]
            return f"https://www.youtube.com/embed/{video_id}"
        return None
