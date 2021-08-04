# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from stories.models import Comment, Recipe
# from django.contrib.auth import get_user_model
# from slugify import slugify
# User = get_user_model()

# @receiver(post_save, sender=Recipe)
# def create_recipe(sender, instance, **kwargs):
#     if instance.is_approved == False:
#         instance.is_approved = True
#         Comment.objects.create(recipe = instance, author= User.objects.filter(is_superuser= True).first(), context='Very Good Recipe')
#         instance.save()