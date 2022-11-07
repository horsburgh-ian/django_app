from django.shortcuts import render

# Create your views here.

from projects.models import Project

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
        }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
        }
    return render(request, 'project_detail.html', context)


def project_projects(request):
    return render(request, 'project_projects.html')


def project_research(request):
    return render(request, 'project_research.html')


def project_course(request):
    return render(request, 'project_course.html')


def project_extra(request):
    return render(request, 'project_extra.html')
