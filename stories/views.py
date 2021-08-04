from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from stories.models import *
from django.contrib import messages
from stories.forms import *
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, TemplateView
)


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

# def home(request):
#     categories = Category.objects.order_by('-created_at')[:3]
#     recent_stories = Story.objects.order_by('-created_at')[:4]
#     holiday_recipes = Recipe.objects.filter(tags__title="Holiday Recipes").order_by('-created_at')[:2]
#     arr = ["Fruits", "Vegetables", "Protein", "Dairy"]
#     context = {
#         "arr": arr,
#         "recent_stories": recent_stories,
#         "holiday_recipes": holiday_recipes,
#         "categories": categories,
#     }
#     return render(request, "index.html", context)


class AboutView(TemplateView):
    template_name = 'about.html'

# def about(request):
#     arr = ["Fruits", "Vegetables", "Protein", "Dairy"]
#     context = {
#         "title": "Delicious Foods", 
#         "description_texts": "Too easy to make", 
#         "daily_visitors": "123", 
#         "stories": "50", 
#         "recipes": "450", 
#         "users_count":"1000",
#         "arr": arr,
#     }
#     return render(request, "about.html", context)



# class StoryListView(TemplateView):
#     template_name = 'stories.html'


class StoryListView(ListView):
    model = Story
    template_name = 'stories.html'
    paginate_by = 1
    context_object_name = 'story_list'
    #queryset = Story.objects.filter(is_published=True)

    def get_queryset(self):
        queryset = super().get_queryset()
        tags = self.request.GET.get('tags')
        queryset = queryset.filter(is_published=True)
        if tags:
            queryset = queryset.filter(tag__id=int(tags))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


# class StoryDetailView(TemplateView):
#     template_name = 'single1.html'

class StoryDetailView(DetailView):
    model = Story
    template_name = 'single1.html'
    context_object_name = 'story'
    queryset = Story.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = Tag.objects.all()
        context['category'] = Category.objects.all()
        context['recent_blog'] = Story.objects.order_by('-created_at')[:5]
        return context


# class RecipeListView(TemplateView):
#     template_name = 'recipes.html'


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes.html'
    paginate_by = 1
    context_object_name = 'recipe_list'
    #queryset = Recipe.objects.filter(is_published=True)

    def get_queryset(self):
        queryset = super().get_queryset()
        tags = self.request.GET.get('tags')
        queryset = queryset.filter(is_published=True)
        if tags:
            queryset = queryset.filter(tag__id=int(tags))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


# class RecipeDetailView(TemplateView):
#     template_name = 'single.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'single.html'
    context_object_name = 'recipe'
    queryset = Recipe.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = Tag.objects.all()
        context['category'] = Category.objects.all()
        context['recent_blog'] = Story.objects.order_by('-created_at')[:3]
        return context


# class ContactView(TemplateView):
#     template_name = 'contact.html'

class ContactView(CreateView):
    form_class = ContactForm
    #fields = '__all__'
    #model = Contact
    template_name = 'contact.html'
    success_url = reverse_lazy('stories:home')

    def form_valid(self, form):
        result = super(ContactView, self).form_valid(form)
        messages.success(self.request, 'Sizin muracietiniz qebul edildi.')
        return result


class CreateRecipeView(TemplateView):
    template_name = 'add_recipe.html'

# class CreateRecipeView(LoginRequiredMixin, CreateView):
#     form_class = RecipeForm
#     template_name = 'add_recipe.html'

#     def form_valid(self, form):
#         result = super(CreateRecipeView, self).form_valid(form)
#         form.instance.author = self.request.user
#         messages.success(self.request, 'Sizin reseptiniz elave olundu.')
#         return result


class CreateStoryView(TemplateView):
    template_name = 'add_story.html'

# class CreateStoryView(LoginRequiredMixin, CreateView):
#     form_class = StoryForm
#     template_name = 'add_story.html'

#     def form_valid(self, form):
#         result = super(CreateStoryView, self).form_valid(form)
#         form.instance.author = self.request.user
#         messages.success(self.request, 'Sizin hekayeniz elave olundu.')
#         return result



class SubscriberView(TemplateView):
    template_name = 'base.html'

# def subscriber(request):
#     form = SubscriberForm()
#     if request.method == 'POST':
#         form = SubscriberForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Siz abune oldunuz.')
#             return redirect(request.META.get("HTTP_REFERER"))
#     context = {
#         'form': form
#     }
#     return render(request,'base.html', context)



# class EditRecipeView(TemplateView):
#     template_name = 'edit-recipe.html'

class EditRecipeView(DetailView):
    model = Recipe
    template_name = 'edit-recipe.html'
    context_object_name = 'recipe'
    # form_class = RecipeForm

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            print(self.get_object())
            return context