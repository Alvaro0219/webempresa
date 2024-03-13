from django.shortcuts import render
from .models import Page

def other(request, page_id):
    page = Page.objects.get(id=page_id)
    return render(request, 'pages/other.html', {'page': page})