from django import forms 
from .models import Contact , Comments , Story,Category
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    name = forms.CharField(label='',max_length=30,widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder': 'Your name',
    }))
    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={
        'class' : 'form-control',
        'placeholder': 'Your Email',
    }))
    subject= forms.CharField(label='',max_length = 60,widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder': 'Your Subject',
    }))
    message = forms.CharField(label='',widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'placeholder': 'Your Message',
        'cols' : '30',
        'rows' : '7',
    })) 
    class Meta:
        model = Contact
        fields = ['name','email','subject','message']


class CommentForm(forms.ModelForm):
    comment = forms.CharField(label = 'Your comment' ,widget=forms.Textarea(attrs={
        'class' : 'form-control'
    }))
    class Meta:
        model = Comments
        fields = ['comment',]



class EditUserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
                'autofocus' : True,
                'class' : 'form-control',
                'placeholder': 'Username'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
                'autofocus' : True,
                'class' : 'form-control',
                'placeholder': 'First name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
                'autofocus' : True,
                'class' : 'form-control',
                'placeholder': 'Last name'
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
                'autofocus' : True,
                'class' : 'form-control',
                'placeholder': 'Description'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
                'autofocus' : True,
                'class' : 'form-control',
                'placeholder': 'Email'
    }))
   
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','description']           




class StoryForm(forms.ModelForm):
    title = forms.CharField(label='',max_length=50,widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder': 'Title',
    }))
    description = forms.CharField(label='',max_length=30,widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'placeholder': 'Description',
    }))
    category = forms.ModelChoiceField(queryset=Category.objects.all(),initial=0,widget=forms.Select(attrs={
        'class' : 'form-control',
        # 'placeholder': 'Description',
    }))
    
    class Meta:
        model= Story
        fields = ['title','description','category','image']