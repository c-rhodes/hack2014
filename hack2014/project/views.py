from django.shortcuts import get_object_or_404
from django.http import (Http404,
                         HttpResponse,
                         HttpResponseRedirect,
                         HttpResponseBadRequest)
from django.views.generic import (DetailView,
                                  ListView,
                                  CreateView,
                                  UpdateView)
from django.core.urlresolvers import reverse_lazy
from django.template.defaultfilters import slugify

from braces.views import LoginRequiredMixin


from project.models import Project, Category


class CategoryList(ListView):
    
    model = Category
    template_name = 'project/category_list.html'
    context_object_name = 'categories'


class CategoryDetail(DetailView):

    model = Category
    template_name = 'project/category_detail.html'


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

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        
        return HttpResponseRedirect(reverse_lazy('projects:project-detail',
            kwargs={'user_id': self.request.user.username, 'slug': self.object.slug}))


class ProjectAddUserUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ['participants']
    template_name_suffix = '_add_user_form'
