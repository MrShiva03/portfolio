from django.shortcuts import render

    # Create your views here.

from main.models import Project,Skill,Certificate

def home(request):
    return render(request, 'home.html',
                {
                    'projects':Project.objects.all(),
                    'skills':Skill.objects.all(), 
                    'cartificates':Certificate.objects.all()  
                })