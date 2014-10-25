from django import forms

from project.models import Project


class ProjectCreateForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name', 'category', 'description', 'date']
