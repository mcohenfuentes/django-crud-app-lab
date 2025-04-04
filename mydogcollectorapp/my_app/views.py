from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Mountain 
from .forms import ClimbForm



@login_required
def mountain_index(request):
    mountains = Mountain.objects.filter(user=request.user)
    return render(request, 'mountains/index.html', {'mountains': mountains})

# def home(request):
#     return render(request, 'home.html')
class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def mountain_detail(request, mountain_id):
    mountain = Mountain.objects.get(id=mountain_id)
    climb_form = ClimbForm()
    return render(request, 'mountains/detail.html', {
        'mountain': mountain, 'climb_form': climb_form})

class MountainCreate(LoginRequiredMixin, CreateView):
    model = Mountain
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class MountainUpdate(LoginRequiredMixin, UpdateView):
    model = Mountain
    fields = ['location', 'description']

class MountainDelete(LoginRequiredMixin, DeleteView):
    model = Mountain
    success_url = '/mountains/'

@login_required
def add_climb(request, mountain_id):
    # create a ModelForm instance using the data in request.POST
    form = ClimbForm(request.POST)
    # validate the form
    if form.is_valid():
        new_climb = form.save(commit=False)
        new_climb.mountain_id = mountain_id
        new_climb.save()
    return redirect('mountain-detail', mountain_id=mountain_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('mountain-index')
        else:
            error_message = 'Invalid sign up - try again'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)