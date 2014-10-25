from django.contrib import admin

from project.models import Category, Project


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user',
                    'description', 'date', 'date_posted')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
