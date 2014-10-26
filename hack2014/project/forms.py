from django import forms

from project.models import Project

from datetimewidget.widgets import DateTimeWidget


class ProjectCreateForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name', 'category', 'description', 'date']
        widgets = {
            'datetime': DateTimeWidget(attrs={'id': 'date'}, bootstrap_version=3)
        }
