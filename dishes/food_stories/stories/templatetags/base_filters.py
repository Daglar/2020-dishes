from django import template
from stories.models import NavLink,SubscribePage , Category ,Comments
from string import capwords
register = template.Library()

@register.simple_tag
def get_nav_links():
    return NavLink.objects.filter(active=True)


@register.simple_tag 
def get_subscribe_page():
    return SubscribePage.objects.all().last()  



@register.simple_tag  
def get_category_list():
    return Category.objects.all()    



@register.filter 
def custom_capitalize(value,mode):
    if mode == 'upper':
        return value.upper()
    elif mode == 'lower':
        return value.lower()    

    
@register.simple_tag
def get_categories():
    return Category.objects.all()


@register.simple_tag
def get_comments(recipe_id):
    return Comments.objects.filter(recipe=recipe_id, reply_comment__isnull=True)


@register.simple_tag
def get_comments_story(story_id):
    return Comments.objects.filter(story=story_id, reply_comment__isnull=True)