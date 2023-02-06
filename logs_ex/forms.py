
from django import forms
from .models import Exercise_Set


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise_Set
        fields = ['exercise_name', 'weight', 'rep_number', 'exertion_level', 'date', 'exercise_category']