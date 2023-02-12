from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Exercise_Set
from .forms import ExerciseForm

def log_home(request):
    exercise_set_list = Exercise_Set.objects.order_by('-date')
    dates = set(exercise_set.date for exercise_set in exercise_set_list)
    date_to_exercise_sets = {date: [] for date in dates}
    for exercise_set in exercise_set_list:
        date_to_exercise_sets[exercise_set.date].append(exercise_set)

    context = {'date_to_exercise_sets': date_to_exercise_sets}
    return render(request, 'logs_ex/log_home.html', context)

def add_log_ex(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logs_ex:log_home')
    else:
        form = ExerciseForm()
    return render(request, 'logs_ex/add_log_ex.html', {'form': form})

def edit_log_ex(request, ex_id):
    log_ex = Exercise_Set.objects.get(pk=ex_id)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, instance=log_ex)
        if form.is_valid():
            form.save()
            return redirect('logs_ex:log_home')
    else:
        form = ExerciseForm(instance=log_ex)
    return render(request, 'logs_ex/edit_log_ex.html', {'form': form, 'log_ex_id': ex_id})

def delete_log_ex(request, ex_id):
    log_ex = get_object_or_404(Exercise_Set, pk=ex_id)
    if request.method == 'POST':
        log_ex.delete()
        return redirect('logs_ex:log_home')
    return render(request, 'logs_ex/delete_log_ex.html', {'log_ex': log_ex})
