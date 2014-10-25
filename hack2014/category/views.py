from django.views.generic import ListView, DetailView

from category.models import Category


class CategoryList(ListView):
    
    model = Category
    template_name = 'category/category_list.html'
    context_object_name = 'categories'


class CategoryDetail(DetailView):

    model = Category
    template_name = 'category/category_detail.html'
