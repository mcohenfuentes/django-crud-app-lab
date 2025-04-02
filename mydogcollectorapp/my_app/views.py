from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class MountainCreate(CreateView):
    model = Mountain
    fields = '__all__'

class MountainUpdate(UpdateView):
    model = Mountain
    fields = ['location', 'description']

class MountainDelete(DeleteView):
    model = Mountain
    success_url = '/mountains/'