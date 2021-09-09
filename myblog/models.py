from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=64)

    def __str__(self):


        return self.name
    def get_absolute_url(self):

        return reverse('home')

class Profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio=models.TextField()
    profile_pic=models.ImageField(null=True,blank=True,upload_to="images/profile/")

    website_url=models.CharField(max_length=255,null=True,blank=True)
    fb_url=models.CharField(max_length=255,null=True,blank=True)
    insta_url=models.CharField(max_length=255,null=True,blank=True)
    linkedin_url=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):

        return reverse('home')

class Post(models.Model):
    title=models.CharField(max_length=255)
    header_image=models.ImageField(null=True,blank=True,upload_to="images/")
    title_tag=models.CharField(max_length=64,default="My Blog")
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=RichTextField(blank=True,null=True)   
    #body=models.TextField()
    post_date=models.DateField(auto_now_add=True)
    snippet=models.CharField(max_length=255)
    category=models.CharField(max_length=255)##add default for admin site adding category
    likes=models.ManyToManyField(User,related_name='bog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + '|' + str(self.author)
    def get_absolute_url(self):
        return reverse("article-detail",args=[str(self.id)]) # if you want to use anyting similar 
                                                               #  to article-detail view defined 
                                                              #in urls template we use reverse

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s'%(self.post.title,self.name)
