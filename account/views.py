from django.views.generic.edit import CreateView, UpdateView, DeleteView,  FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Project

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class CustomLoginView(LoginView):
    template_name = 'Login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('projectlist')


class RegisterPage(FormView):
    template_name = 'Register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('projectlist')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)


class ListProjects(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = 'projectlist'
    template_name = 'ListProject.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projectlist'] = context['projectlist'].filter(user=self.request.user)
        context['projectlist'] = context['projectlist'].order_by('-project_time')
        context['count'] = context['projectlist'].count()
        return context
    
  
class CreateProject(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['project_name','project_units','project_area']
    template_name = 'CreateProject.html'
    success_url = reverse_lazy('projectlist')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateProject, self).form_valid(form)


class ProjectDetail(LoginRequiredMixin, DetailView):
    model = Project
    fields = '__all__'
    context_object_name = 'projectdetail'
    template_name = 'ProjectDetail.html'


class ProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ['project_name','project_units','project_area']
    template_name = 'ProjectUpdate.html'
    success_url = reverse_lazy('projectlist')


class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = "ProjectDelete.html"
    success_url = reverse_lazy('projectlist')

