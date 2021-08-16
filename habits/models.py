from django.db import models

class Habit(models.Model):
  title = models.CharField(max_length=100)
  is_completed = models.BooleanField()
  times_completed = models.IntegerField()


