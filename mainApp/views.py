from django.shortcuts import render

def playGame(request):
    dictV = {}
    return render(request, 'playGame.html', dictV)

def playGame2(request):
    dictV = {}
    return render(request, 'playGame2.html', dictV)
