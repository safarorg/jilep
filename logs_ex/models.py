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
    exercise_name = models.CharField(max_length=40)
    weight = models.IntegerField()
    rep_number = models.IntegerField()
    exertion_level = models.IntegerField()
    date = models.DateTimeField()
    exercise_category = models.ForeignKey(Exercise_Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name + str(self.weight) + str(self.number_of_reps)


# from django.db import models


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)