from django.shortcuts import render

def home(request):
    return render(request, 'core/index.html')

def visit(request):
    return render(request, 'core/visit.html')

def history(request):
    return render(request, 'core/history.html')
