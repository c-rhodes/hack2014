from django.db import models

from users.models import User


class Category(models.Model):

   class Meta:
       verbose_name_plural = 'Categories'

   name = models.CharField(max_length=32, help_text='The name of the category') 

   def __str__(self):
       return self.name


class Project(models.Model):
    name = models.CharField(max_length=128, help_text='A short name identifying the project')
    user = models.ForeignKey(User, related_name='projects')
    category = models.ManyToManyField(Category)
    description = models.TextField()
    participants = models.ManyToManyField(User, blank=True, null=True)
    date = models.DateTimeField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
