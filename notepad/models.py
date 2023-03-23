from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Plan(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Reja'
        verbose_name_plural = 'Rejalar'