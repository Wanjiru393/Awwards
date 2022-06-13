# from django.db import models
# from django.contrib.auth.models import User

# # Create your models here.
# class Profile(models.Model):
#     username = models.CharField(max_length=40,blank=True)
#     bio = models.TextField(max_length=300)
#     prof_pic = models.ImageField(upload_to="profile/")

#     def __str__(self):
#         return self.username + " " + self.bio 
  

# class Project(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.CharField(max_length=500)

#     def __str__(self):
#         return self.name + " " + self.description
    

from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q

import datetime as dt

# Create your models here.
class categories(models.Model):
    categories= models.CharField(max_length=100)

    def __str__(self):
        return self.categories

    def save_category(self):
        self.save()

    @classmethod
    def delete_category(cls,categories):
        cls.objects.filter(categories=categories).delete()


class technologies(models.Model):
    technologies = models.CharField(max_length=100)

    def __str__(self):
        return self.technologies

    def save_technology(self):
        self.save()

    @classmethod
    def delete_technology(cls,technologies):
        cls.objects.filter(technologies=technologies).delete()


class Project(models.Model):
    title = models.CharField(max_length=150)
    landing_page = models.ImageField(upload_to='landingpage/')
    description = HTMLField()
    link= models.CharField(max_length=255)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    screenshot1 = models.ImageField(upload_to='screenshots/')
    screenshot2 = models.ImageField(upload_to='screenshots/')
    design = models.IntegerField(blank=True,default=0)
    usability = models.IntegerField(blank=True,default=0)
    creativity = models.IntegerField(blank=True,default=0)
    content = models.IntegerField(blank=True,default=0)
    overall_score = models.IntegerField(blank=True,default=0)
    technologies = models.ManyToManyField(technologies)
    categories = models.ManyToManyField(categories)
    post_date = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to='avatars/')

    def __str__(self):
        return self.title

    @classmethod
    def search_project(cls,search_term):
        projects = cls.objects.filter(Q(username__username=search_term) | Q(title__icontains=search_term) | Q(country__countries=search_term) | Q(overall_score__icontains=search_term))
        return projects


class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatars/')
    description = HTMLField()
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Rating(models.Model):
    design = models.IntegerField(blank=True,default=0)
    usability = models.IntegerField(blank=True,default=0)
    creativity = models.IntegerField(blank=True,default=0)
    content = models.IntegerField(blank=True,default=0)
    overall_score = models.IntegerField(blank=True,default=0)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)