from django.shortcuts import render

def playground(request):
    return render(request, 'playground/playground.html')

