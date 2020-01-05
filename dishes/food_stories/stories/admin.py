from django.contrib import admin
from .models import AboutPage,AboutPagePicture, NavLink ,SubscribePage ,Contact,Story,Category,Recipes , Comments
# Register your models here.


admin.site.register(AboutPagePicture)

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    fields= ('title','description',)
    search_fields=('title',)
    list_filter=('created_at',)
    list_display=('title','description',)
    # readonly_fields=('title',)
    # ordering=('-created_at',)




@admin.register( NavLink)
class NavLinksAdmin(admin.ModelAdmin):
    fields=('title','url','active',)
    list_filter=('active',)
    list_display=('title','url','active',)


@admin.register(SubscribePage)
class SubscribePageAdmin(admin.ModelAdmin):
    fields=('title','description',)
    list_filter=('title',)
    list_display=('title','description',)



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    field = ('name','email','subject', 'message',)
    list_filter = ('created_at',)
    list_display = ('name','email','subject',)


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    fields=('title','image','description','category','owner',)
    list_display = ('title','category',)
    list_filter = ('created_at',)
    search_field = ('title',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields=('title','image',)
    list_display = ('title',)
    search_field = ('title',)

@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    fields=('title','image','description','category','long_description','owner',)
    list_display = ('title','category',)
    list_filter = ('created_at',)
    search_field = ('title',)



@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','recipe','story')