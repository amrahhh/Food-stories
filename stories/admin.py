from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from stories.models import (
    Story,
    Recipe,
    Category,
    Review,
    Comment,
    Contact,
    Subscriber,
    Tag,
)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at',)
    search_fields = ('name', 'email', 'subject', 'message',)

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category',)
    list_filter = ('category',)
    search_fields = ('title', 'description',)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'description')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('context',)
    search_fields = ('context',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('context',)
    search_fields = ('context',)

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    search_fields = ('email',)

class TagAdmin(TranslationAdmin):
    search_fields = ('title',)
    list_display = ('id', 'title', 'created_at')

class CategoryAdmin(TranslationAdmin):
    search_fields = ('title',)
    list_display = ('id', 'title', 'created_at')

admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)