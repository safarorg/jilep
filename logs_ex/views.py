from django.shortcuts import render, get_object_or_404
from .models import Exercise_Set
from .forms import ExerciseForm

def index(request):
    exercise_set_list = Exercise_Set.objects.order_by('-date')[:5]
    context = {'exercise_set_list': exercise_set_list}
    return render(request, 'logs_ex/index.html', context)

def add_log_ex(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ExerciseForm()
    return render(request, 'logs_ex/add_log_ex.html', {'form': form})

def log_ex_detail(request, ex_id):
    log_ex = Exercise_Set.objects.get(pk=ex_id)
    return render(request, 'logs_ex/log_detail.html', {'log_ex':log_ex})