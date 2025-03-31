from django.shortcuts import render



class Mountain:
    def __init__(self, name, location, description):
        self.name = name
        self.location = location
        self.description = description
        


mountains = [
    Mountain('Saint Elias', 'North America', 'Second Tallest Mountain in North America'),
    Mountain('Denali', 'North America', 'Highest Peak'),
    Mountain('Mount Ranier', 'North America', 'Beautiful'),
]

def mountain_index(request):
    # Render the cats/index.html template with the cats data
    return render(request, 'mountains/index.html', {'mountains': mountains})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')