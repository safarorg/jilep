from django.db import models
from django.contrib.auth.models import User

EXERCISE_CATEGORY_CHOICES = (
    ("None", "None"),
    ("Chest", "Chest"),
    ("Biceps", "Biceps"),
    ("Triceps", "Triceps"),
    ("Shoulders", "Shoulders"),
    ("Back", "Back"),
    ("Legs", "Legs"),
    ("Abs", "Abs"),
)

class Exercise_Category(models.Model):
    name = models.CharField(max_length=50, choices=EXERCISE_CATEGORY_CHOICES, default="None")

    def __str__(self):
        return self.name

class Exercise_Set(models.Model):
    exercise_name = models.CharField(max_length=40)
    weight = models.IntegerField()
    number_of_reps = models.IntegerField()
    exertion_level = models.IntegerField()
    date = models.DateTimeField()
    exercise_category = models.ForeignKey(Exercise_Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.exercise_name + str(self.weight) + str(self.number_of_reps)