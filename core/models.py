from django.db import models
from django.shortcuts import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify 
from annoying.fields import AutoOneToOneField
from django.utils import timezone

CATEGORY_CHOICES = (
    ('E', 'Electronics'),
    ('F', 'Fashion'),
    ('HAB', 'Health and Beauty'),
    ('HAG', 'House and Garden'),
    ('S', 'Sports'),
    ('A', 'Auto'),
    ('O', 'Others')
)

class Location(models.Model):
    region = models.CharField(max_length=29)
    area = models.CharField(max_length=25)
    city = models.CharField(max_length=27)
    street = models.CharField(max_length=132)


    def __str__(self):
        return '%s, %s' % (self.city, self.street)


class Item(models.Model):
    img = models.ImageField(upload_to='images/', default='/images/default.jpg')
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(default=timezone.now) 
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField()
    location = models.OneToOneField(Location, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Item, self).save(*args, **kwargs)
        self.slug = slugify('product'+str(self.id))
        super(Item, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={"slug": self.slug})

class Profile(models.Model):
    user = AutoOneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super(Profile, self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("core:profile", kwargs={"slug": self.slug})