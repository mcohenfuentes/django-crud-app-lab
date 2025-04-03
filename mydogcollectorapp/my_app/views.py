from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Mountain 
from .forms import ClimbForm




def mountain_index(request):
    mountains = Mountain.objects.all()
    return render(request, 'mountains/index.html', {'mountains': mountains})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def mountain_detail(request, mountain_id):
    mountain = Mountain.objects.get(id=mountain_id)
    climb_form = ClimbForm()
    return render(request, 'mountains/detail.html', {
        'mountain': mountain, 'climb_form': climb_form})

class MountainCreate(CreateView):
    model = Mountain
    fields = '__all__'

class MountainUpdate(UpdateView):
    model = Mountain
    fields = ['location', 'description']

class MountainDelete(DeleteView):
    model = Mountain
    success_url = '/mountains/'

def add_climb(request, mountain_id):
    # create a ModelForm instance using the data in request.POST
    form = ClimbForm(request.POST)
    # validate the form
    if form.is_valid():
        new_climb = form.save(commit=False)
        new_climb.mountain_id = mountain_id
        new_climb.save()
    return redirect('mountain-detail', mountain_id=mountain_id)