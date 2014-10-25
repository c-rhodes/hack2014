from django.http import Http404
from django.views.generic import (DetailView,
                                  ListView,
                                  CreateView)

from braces.views import LoginRequiredMixin


from project.models import Project


class ProjectView(DetailView):
    
    model = Project
    template_name = 'project/detail.html'

    def get_context_data(self, **kwargs):        
        context = super(ProjectView, self).get_context_data(**kwargs)
        return context

    def get_object(self, queryset=None):
        obj = super(ProjectView, self).get_object()

        if obj.user.username != self.kwargs.get('user_id'):
            raise Http404

        return obj


class ProjectListView(ListView):
    
    model = Project
    template_name = 'project/projects.html'
    context_object_name = 'projects'


class UserProjectListView(ListView):

    model = Project
    template_name = 'project/user_projects_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        queryset = Project.objects.filter(user__username=self.kwargs.get('user_id'))
        return queryset


class ProjectCreateView(LoginRequiredMixin, CreateView):

    model = Project
    fields = ['name', 'category', 'description', 'date']


