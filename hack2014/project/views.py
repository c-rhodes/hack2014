from django.shortcuts import get_object_or_404
from django.http import (Http404,
                         HttpResponse,
                         HttpResponseRedirect,
                         HttpResponseBadRequest)

from django.views.generic import (View,
                                  DetailView,
                                  ListView,
                                  CreateView,
                                  UpdateView,
                                  TemplateView)
from django.core.urlresolvers import reverse_lazy
from django.template.defaultfilters import slugify

from braces.views import LoginRequiredMixin


from project.models import Project


class ProjectView(DetailView):
    
    model = Project
    template_name = 'project/project_detail.html'

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
    fields = ['name', 'category', 'description', 'date', 'address_first', 'address_second', 'address_third', 'city', 'postcode']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        
        return HttpResponseRedirect(reverse_lazy('projects:project-detail',
            kwargs={'user_id': self.request.user.username, 'slug': self.object.slug}))


class ProjectAddUserUpdateView(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        project = Project.objects.get(id=kwargs.get('project_id'))

        if request.user != project.user or request.user in project.participants.all():
            project.participants.add(request.user)
            project.save()
        else:
            return HttpResponse(status=400) # bad request
        return HttpResponseRedirect(reverse_lazy('projects:project-detail', kwargs={'user_id': project.user.username, 'slug': project.slug}))
