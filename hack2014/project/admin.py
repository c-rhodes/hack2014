from django.contrib import admin

from project.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user',
                    'description', 'date', 'date_posted')


admin.site.register(Project, ProjectAdmin)
