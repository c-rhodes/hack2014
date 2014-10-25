from django.db import models
from django.template.defaultfilters import slugify

from users.models import User
from category.models import Category


class Project(models.Model):
    name = models.CharField(max_length=128, help_text='A short name identifying the project')
    user = models.ForeignKey(User, related_name='projects')
    category = models.ManyToManyField(Category)
    description = models.TextField()
    participants = models.ManyToManyField(User, blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    date = models.DateTimeField()
    date_posted = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
