from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField("Назва події", max_length=200)
    description = models.TextField("Опис", blank=True)
    date = models.DateField("Дата події")
    time = models.TimeField("Час", blank=True, null=True)
    location = models.CharField("Місце проведення", max_length=200, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date', 'time']
        verbose_name = "Подія"
        verbose_name_plural = "Події"

    def __str__(self):
        return f"{self.title} ({self.date})"
