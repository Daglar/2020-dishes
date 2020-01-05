from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField


# Create your models here.

class AboutPage(models.Model):
    title = models.CharField(max_length=255,blank=False,null=True)
    description = models.TextField(blank=False,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    



class AboutPagePicture(models.Model):
    first_image = models.ImageField(upload_to='proj_pics')
    second_image = models.ImageField(upload_to='proj_pics',default='')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
 


class NavLink(models.Model):
    title = models.CharField(max_length=255,blank=False,null=False) 
    url = models.CharField(max_length=255,blank=True)
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class SubscribePage(models.Model):
    title = models.CharField(max_length=255,blank=False,null=True)
    description = models.TextField(blank=False,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField('Ad',max_length=30,blank=False,null=False)
    email = models.EmailField(blank=False,null=False)
    subject= models.CharField(max_length = 60 , blank = False  , null = False)
    message = models.TextField(blank = False  , null = False)

    updated_at = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name


class Story(models.Model):
    title = models.CharField(max_length=50,blank=False,null=True)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='stories',blank=False,null=True)
    description = models.TextField(blank=False)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,related_name='stori',null=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='stories',default=2)
    updated_at = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name='hekaye'
        verbose_name_plural = 'hekayeler'
        ordering = ('-created_at',)



class Category(models.Model):
    title = models.CharField(max_length=50,blank=False,null=True)
    image = models.ImageField(upload_to='categories',blank=False)

    updated_at = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
         return self.title



class Recipes(models.Model):
    title = models.CharField(max_length=50,blank=False,null=True)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='recipes',blank=False,null=True)
    description = models.TextField(blank=False)
    long_description = RichTextField('Longdescription')
    category = models.ForeignKey('Category',on_delete=models.CASCADE,related_name='recipes',null=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='recipes',default=2)
    updated_at = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Resept'
        verbose_name_plural = 'Reseptler'
        ordering = ('-created_at',)



class Comments(models.Model):
    user = models.ForeignKey(User,related_name = 'comment',on_delete=models.CASCADE)
    comment = models.TextField('comment')
    recipe = models.ForeignKey(Recipes,related_name = 'comment',on_delete=models.CASCADE,null=True,blank=True)
    story = models.ForeignKey(Story,related_name = 'comment',on_delete=models.CASCADE,null=True,blank=True)
    reply_comment = models.ForeignKey('self',related_name = 'reply_comments',on_delete=models.CASCADE,null=True,blank=True)


    updated_at = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user.first_name}+{self.user.last_name}"

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Rey'
        verbose_name_plural = 'Reyler'    
