from django.urls import path
from .views import *
app_name = 'stories'

urlpatterns=[
    path('',IndexView.as_view(),name='index'),
    path('about/',AboutView.as_view(),name='about'),
    path('stories/',StoriesView.as_view(),name='stories'),
    path('recipes/',RecipesView.as_view(),name='recipes'),
    path('create-story/<int:pk>/',CreateStoryView.as_view(),name='create-story'),
    path('contact/',ContactView.as_view(),name='contact'),
    path('user-profile/<int:pk>/',UserProfileView.as_view(),name='user-profile'),
    path('user-edit/<int:pk>/',UserEditView.as_view(),name='user-edit'),
    # path('single/<int:pk>/',single,name='single'),
    path('single/<int:pk>/',RecipesDetailView.as_view(),name='single'),
    path('stories-single/<int:pk>/',StoriesDetailView.as_view(),name='stories-single'),
    path('index-single/<int:pk>/',RecentPostsDetailView.as_view(),name='index-single'),
    path('user-single/<int:pk>/',UserPostsDetailView.as_view(),name='user-single'),



]