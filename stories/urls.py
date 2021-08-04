from django.urls import path
from stories.views import *

app_name = 'stories'

urlpatterns = [    
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('stories/', StoryListView.as_view(), name='stories'),
    path('stories/<slug:slug>/', StoryDetailView.as_view(), name='story_detail'), 
    path('contact/', ContactView.as_view(), name="contact"),    
    path('create-story/', CreateStoryView.as_view(), name="create_story"),
    path('create-recipe/', CreateRecipeView.as_view(), name="create_recipe"),
    path('subscriber/', SubscriberView.as_view(), name='subscriber'),
    path('recipes/', RecipeListView.as_view(), name="recipes"),
    path('recipes/<slug:slug>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('edit-recipe/<int:pk>/', EditRecipeView.as_view(), name='edit_recipe'),
]