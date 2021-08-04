from rest_framework.response import Response
from rest_framework import status
from stories.models import Recipe, Story, Category, Comment, Subscriber, Tag
from stories.api.serializers import RecipeSerializer, RecipeCreateSerializer, StorySerializer, StoryCreateSerializer, CategorySerializer, CategoryCreateSerializer, CommentSerializer, CommentCreateSerializer, SubscriberSerializer, TagSerializer

# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

import json

from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from accounts.api.serializers import UserSerializer


# -----------Method 3 ---------------------


# Class Based
class SubscribeAPIView(CreateAPIView):
    queryset = Subscriber.objects.filter(is_active=True)
    serializer_class = SubscriberSerializer

class TagAPIView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CommentAPIView(APIView):

    def get(self,request,*args,**kwargs):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment , many = True , context = {'request':request})
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        recipe_data = request.data
        recipe_id = kwargs.get('pk')
        recipe = Recipe.objects.filter(pk=recipe_id).first()
        serializer = CommentSerializer(data=recipe_data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(recipe=recipe)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentDetailAPIView(APIView):
    
    def get(self,request,*args,**kwargs):
        comment_id = kwargs.get('pk')
        comment = Comment.objects.filter(pk=comment_id)
        serializer = CommentSerializer(comment , many = True , context = {'request':request})
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        comment_id = kwargs.get('pk')
        comment = Comment.objects.filter(pk=comment_id).first()
        serializer = CommentCreateSerializer(comment, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        comment_id = kwargs.get('pk')
        comment = Comment.objects.filter(pk=comment_id).first()
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RecipeAPIView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        recipes = Recipe.objects.filter(is_published=True)
        filter_by = json.loads(json.dumps(request.GET))
        if filter_by:
            recipes = recipes.filter(**filter_by)  # title=resept
        serializer = RecipeSerializer(recipes, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        recipe_data = request.data
        serializer = RecipeCreateSerializer(data=recipe_data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RecipeDetailAPIView(APIView):
    permission_classes= (IsAuthenticatedOrReadOnly,)
    def get(self, request, *args, **kwargs):
        recipe_id = kwargs.get('pk')
        recipe = Recipe.objects.filter(pk=recipe_id, is_published=True).first()
        if not recipe:
            raise NotFound
        serializer = RecipeSerializer(recipe, context={'request': request})
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        recipe_data = request.data
        recipe_id = kwargs.get('pk')
        recipe = Recipe.objects.filter(pk=recipe_id, is_published=True).first()
        if not recipe:
            raise NotFound
        serializer = RecipeCreateSerializer(data=recipe_data, instance=recipe, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        recipe_data = request.data
        recipe_id = kwargs.get('pk')
        recipe = Recipe.objects.filter(pk=recipe_id, is_published=True).first()
        if not recipe:
            raise NotFound
        serializer = RecipeCreateSerializer(data=recipe_data, instance=recipe,
                                            partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        recipe_id = kwargs.get('pk')
        recipe = Recipe.objects.filter(pk=recipe_id, is_published=True)
        if not recipe:
            raise NotFound
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#    -------------Story--------------

class StoryAPIView(APIView):

    def get(self, request, *args, **kwargs):
        recipes = Story.objects.filter(is_published=True)
        filter_by = json.loads(json.dumps(request.GET))
        if filter_by:
            recipes = recipes.filter(**filter_by)  # title=resept
        serializer = StorySerializer(recipes, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        recipe_data = request.data
        serializer = StoryCreateSerializer(data=recipe_data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StoryDetailAPIView(APIView):

    def get(self, request, *args, **kwargs):
        recipe_id = kwargs.get('pk')
        recipe = Story.objects.filter(pk=recipe_id, is_published=True).first()
        if not recipe:
            raise NotFound
        serializer = StorySerializer(recipe, context={'request': request})
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        recipe_data = request.data
        recipe_id = kwargs.get('pk')
        recipe = Story.objects.filter(pk=recipe_id, is_published=True).first()
        if not recipe:
            raise NotFound
        serializer = StoryCreateSerializer(data=recipe_data, instance=recipe, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        recipe_data = request.data
        recipe_id = kwargs.get('pk')
        recipe = Story.objects.filter(pk=recipe_id, is_published=True).first()
        if not recipe:
            raise NotFound
        serializer = StoryCreateSerializer(data=recipe_data, instance=recipe,
                                            partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        recipe_id = kwargs.get('pk')
        recipe = Story.objects.filter(pk=recipe_id, is_published=True)
        if not recipe:
            raise NotFound
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#  ----------- Category --------------------

class CategoryAPIView(APIView):

    def get(self, request, *args, **kwargs):
        recipes = Category.objects.all()
        filter_by = json.loads(json.dumps(request.GET))
        if filter_by:
            recipes = recipes.filter(**filter_by)  # title=resept
        serializer = CategorySerializer(recipes, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        recipe_data = request.data
        serializer = CategoryCreateSerializer(data=recipe_data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CategoryDetailAPIView(APIView):

    def get(self, request, *args, **kwargs):
        recipe_id = kwargs.get('pk')
        recipe = Category.objects.filter(pk=recipe_id).first()
        if not recipe:
            raise NotFound
        serializer = CategorySerializer(recipe, context={'request': request})
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        recipe_data = request.data
        recipe_id = kwargs.get('pk')
        recipe = Category.objects.filter(pk=recipe_id).first()
        if not recipe:
            raise NotFound
        serializer = CategoryCreateSerializer(data=recipe_data, instance=recipe, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        recipe_data = request.data
        recipe_id = kwargs.get('pk')
        recipe = Category.objects.filter(pk=recipe_id).first()
        if not recipe:
            raise NotFound
        serializer = CategoryCreateSerializer(data=recipe_data, instance=recipe,
                                            partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        recipe_id = kwargs.get('pk')
        recipe = Category.objects.filter(pk=recipe_id)
        if not recipe:
            raise NotFound
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# -----------Method 2 ---------------------


# class RecipeList(ListCreateAPIView):
#     queryset = Recipe.objects.filter(is_published=True)
#     serializer_class = RecipeSerializer

#     def get_serializer_class(self):
#         if self.request.method == 'GET':
#             return self.serializer_class
#         return RecipeCreateSerializer


# class RecipeDetail(RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = Recipe.objects.filter(is_published=True)
#     serializer_class = RecipeSerializer

#     def get_serializer_class(self):
#         if self.request.method == 'GET':
#             return self.serializer_class
#         return RecipeCreateSerializer


# class StoryList(ListCreateAPIView):
#     queryset = Recipe.objects.filter(is_published=True)
#     serializer_class = RecipeSerializer

#     def get_serializer_class(self):
#         if self.request.method == 'GET':
#             return self.serializer_class
#         return RecipeCreateSerializer


# class StoryDetail(RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = Recipe.objects.filter(is_published=True)
#     serializer_class = RecipeSerializer

#     def get_serializer_class(self):
#         if self.request.method == 'GET':
#             return self.serializer_class
#         return RecipeCreateSerializer



# -----------Method 1 ---------------------


# @api_view(('GET', 'POST'))
# def recipes(request):
#     if request.method == 'POST':
#         recipe_data = request.data
#         serializer = RecipeCreateSerializer(data=recipe_data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     recipes = Recipe.objects.filter(is_published=True)
#     serializer = RecipeSerializer(recipes, many=True, context={'request': request})

#     # serialized_recipe_list = [recipe.serialized_data for recipe in recipes]
#     # json_data = {
#     #     'recipes': serialized_recipe_list
#     # }
#     return Response(serializer.data)


# @api_view(('GET', 'POST'))
# def stories(request):
#     if request.method == 'POST':
#         recipe_data = request.data
#         serializer = StoryCreateSerializer(data=recipe_data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     recipes = Story.objects.filter(is_published=True)
#     serializer = StorySerializer(recipes, many=True, context={'request': request})

#     # serialized_recipe_list = [recipe.serialized_data for recipe in recipes]
#     # json_data = {
#     #     'recipes': serialized_recipe_list
#     # }

#     return Response(serializer.data)

# @api_view(['GET', 'PUT', 'DELETE'])
# def recipe_detail(request, slug):
#     try:
#         recipe = Recipe.objects.get(slug=slug)
#     except Recipe.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = RecipeSerializer(recipe)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = RecipeSerializer(recipe, data=request.data, partial= True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         recipe.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# @api_view(['GET', 'PUT', 'DELETE'])
# def story_detail(request, slug):
#     try:
#         recipe = Story.objects.get(slug=slug)
#     except Story.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = StorySerializer(recipe)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = StorySerializer(recipe, data=request.data, partial= True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         recipe.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)