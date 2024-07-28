from django.shortcuts import render


def competitions(request):
    return render(request, 'competitions/competitions.html')

