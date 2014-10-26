from django.db import models
from django.template.defaultfilters import slugify

from users.models import User
from category.models import Category
import requests


class Project(models.Model):
    name = models.CharField(max_length=128, help_text='A short name identifying the project')
    user = models.ForeignKey(User, related_name='projects')
    category = models.ManyToManyField(Category)
    description = models.TextField()
    participants = models.ManyToManyField(User, blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    date = models.DateTimeField()
    date_posted = models.DateTimeField(auto_now_add=True)

    address_first = models.TextField(max_length=200)
    address_second = models.TextField(max_length=200, blank=True, null=True)
    address_third = models.TextField(max_length=200, blank=True, null=True)
    city = models.TextField(max_length=200)
    postcode = models.TextField(max_length=15)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def getLatLon(self, address):
        url = "http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=%s" % (address)
        r = requests.get(url)
        return r.text

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        geo = json.loads(self.getLatLon("%s,%s,%s,%s %s" % (self.address_first, self.address_second, self.address_third, self.city, self.postcode)))
        if geo['status'] == "OK":
            self.latitude = geo['results'][0]['geometry']['location']['lat']
            self.longitude = geo['results'][0]['geometry']['location']['lng']

        super(Project, self).save(*args, **kwargs)


    def __str__(self):
        return self.name
