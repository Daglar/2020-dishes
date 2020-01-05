from django.shortcuts import render
from django.contrib import messages
from .models import AboutPage, AboutPagePicture, Recipes , Story ,Category
from django.contrib.auth.models import User
from django.views.generic import ListView,CreateView , DetailView 
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin,UpdateView
from .forms import *

# def index(request):

#     return render(request,'index.html')


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["content"] = Story.objects.all().order_by('-created_at')[:4]
        
        context["user_post"] = Story.objects.filter()
        print(context)
        return context
    






class AboutView(TemplateView):
    template_name='about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["content"] = AboutPage.objects.last()

        img = AboutPagePicture.objects.all()
        images=[]
        for i in img:
            images.append(i.first_image)
            images.append(i.second_image)
            context['images'] = images
        return context
    

# def recipes(request):
#     recipes = Recipes.objects.all()
#     context = {
#         'recipes' : recipes
#     }
#     return render(request,'recipes.html',context)




# def recipes(request):
#     recipes = Recipes.objects.all()
#     paginator = Paginator(recipes, 3) # 3 posts in each page
#     page = request.GET.get('page')
#     try:
#         recipes = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer deliver the first page
#         recipes = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range deliver last page of results
#         recipes = paginator.page(paginator.num_pages)

#     context = {
#         'page' : page,
#         'recipes' : recipes
#     }    
#     return render(request,'recipes.html',context)



class CreateStoryView(CreateView):
    model = Story
    form_class = StoryForm
    template_name = 'create-story.html'


    def form_valid(self,form):
        story = form.save(commit=False)
        story.owner = self.request.user
        story.save()
        self.success_url = reverse_lazy('stories:user-profile',kwargs={'pk': self.request.user.id})
        return super().form_valid(form)


class RecipesView(ListView):
    model = Recipes
    template_name = 'recipes.html'
    context_object_name = 'recipes'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["categories"] = Category.objects.all() 
        return context

   

  



class StoriesView(ListView):
    model = Story
    template_name = 'stories.html'
    context_object_name = 'stories' 
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    
  



 

# def contact(request):
#     form = ContactForm
#     if request.method=='POST':
#         f = ContactForm(data=request.POST)
#         if f.is_valid():
#             f.save()
#             messages.success(request, 'Form submission successful')
#             # context['success'] = 'success'
#         else:
#             context['form'] = form.errors

#     context = {
#         'form' : form
#     }
#     return render(request,'contact.html',context)            
class ContactView(CreateView):
    model = Contact
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('stories:contact')

# def single(request,pk):
#     recipe =  Recipes.objects.get(id=pk)
#     context = {
#        'recipe_data' : recipe,
#    }

#     return render(request,'single.html',context)    

class RecipesDetailView(FormMixin, DetailView):
    model = Recipes
    context_object_name = 'recipe_data'
    template_name = 'single.html'
    form_class = CommentForm 
    


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            print('----------------------------------------------------------------------')
            return self.form_valid(form)
        else:
            print('u----------------------------------------------------------------------')
            return self.form_invalid(form)


    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.recipe = self.object
        comment.save()
        self.success_url = reverse_lazy('stories:single', kwargs={'pk':self.object.id})
        return super().form_valid(form)

    def get_user_full_name(self):
        return "{} {}".format(self.User.first_name,self.User.last_name)    





 



class StoriesDetailView(FormMixin, DetailView):
    model = Story
    context_object_name = 'stories_data'
    template_name = 'stories-single.html'
    form_class = CommentForm 
    


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.recipe = self.object
        comment.save()
        self.success_url = reverse_lazy('stories:stories-single', kwargs={'pk':self.object.id})
        return super().form_valid(form)

    def get_user_full_name(self):
        return "{} {}".format(self.User.first_name,self.User.last_name)




class RecentPostsDetailView(FormMixin, DetailView):
    model = Story
    context_object_name = 'stories_data'
    template_name = 'index-single.html'
    form_class = CommentForm 
    


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.recipe = self.object
        comment.save()
        self.success_url = reverse_lazy('stories:stories-single', kwargs={'pk':self.object.id})
        return super().form_valid(form)

    def get_user_full_name(self):
        return "{}".format(self.User.username)




# def user_profile(request):
#     return render(request,'user_profile.html')



class UserProfileView(DetailView):
    model = User
    template_name = 'user_profile.html'    




class UserEditView(UpdateView):
    model = User
    template_name = 'user-edit.html'
    form_class = EditUserForm



    def get_success_url(self):
        return reverse_lazy('stories:user-profile',kwargs={'pk': self.object.pk})




class UserPostsDetailView(FormMixin, DetailView):
    model = Story
    context_object_name = 'user_data'
    template_name = 'userpostdetail.html'
    form_class = CommentForm 
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.user)
        context["content"] = Story.objects.all().filter(owner=self.request.user)
        print(context)
        return context
    

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.recipe = self.object
        comment.save()
        self.success_url = reverse_lazy('stories:user-single', kwargs={'pk':self.object.id})
        return super().form_valid(form)

    def get_user_full_name(self):
        return "{}".format(self.User.username)