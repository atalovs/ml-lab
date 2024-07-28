from django.shortcuts import render
from .models import Lesson

def lessons(request):
    lessons_list = Lesson.objects.all()
    return render(request, 'lessons/lessons.html', {'lessons': lessons_list})
