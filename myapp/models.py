# myapp/models.py

# myapp/models.py
from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100)
    sound = models.CharField(max_length=100)

    def speak(self):
        return f'The {self.name} says "{self.sound}"'


