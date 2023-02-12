
from django import forms
from .models import Exercise_Set


class ExerciseForm(forms.ModelForm):
    date = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'date'}))
    class Meta:
        model = Exercise_Set
        fields = ['exercise_name', 'weight', 'number_of_reps', 'exertion_level', 'date', 'exercise_category']