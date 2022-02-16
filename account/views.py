from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Project


class ListProjects(ListView):
    model = Project
    context_object_name = 'projectlist'
    template_name = 'ListProject.html'
    
class CreateProject(CreateView):
    model = Project
    fields = '__all__'
    template_name = 'CreateProject.html'
    success_url = reverse_lazy('listproject')

class ProjectDetail(DetailView):
    model = Project
    fields = '__all__'
    context_object_name = 'projectdetail'
    template_name = 'ProjectDetail.html'

class ProjectUpdate(UpdateView):
    model = Project
    fields = '__all__'
    template_name = 'ProjectUpdate.html'
    success_url = reverse_lazy('listproject')
    
class ProjectDelete(DeleteView):
    model = Project
    template_name = "ProjectDelete.html"
    success_url = reverse_lazy('listproject')
