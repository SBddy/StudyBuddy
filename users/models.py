from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    study_subjects = models.TextField(blank=True)  # Интересующие предметы
    study_level = models.CharField(max_length=50, blank=True)  # Уровень (школьник, студент)
    bio = models.TextField(blank=True)  # Короткое описание о себе

    def __str__(self):
        return self.username
