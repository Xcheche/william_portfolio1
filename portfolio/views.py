from django.shortcuts import render

# Create your views here.
from .models import Project

def home(request):
    # return HttpResponse("Hello, world. You're at the portfolio index.")
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})


