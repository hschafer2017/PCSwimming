from django.shortcuts import render

# Create your views here.
def get_index(request): 
    return render(request, 'home/index.html')

