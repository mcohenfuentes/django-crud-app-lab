from django.shortcuts import render
from .models import Mountain 




def mountain_index(request):
    mountains = Mountain.objects.all()
    return render(request, 'mountains/index.html', {'mountains': mountains})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def mountain_detail(request, mountain_id):
    mountain = Mountain.objects.get(id=mountain_id)
    return render(request, 'mountains/detail.html', {'mountain': mountain})