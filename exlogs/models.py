from django.db import models

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

class Exercise_Set(models.Model):
    name = models.CharField(max_length=40)
    weight = models.IntegerField()
    number_of_reps = models.IntegerField()
    exertion_level = models.CharField(max_length=40)
    category = models.ForeignKey(Exercise_Category, on_delete=models.CASCADE)