from django.urls import path
from stories.api.views import RecipeAPIView, RecipeDetailAPIView, StoryAPIView, StoryDetailAPIView, CategoryAPIView, CategoryDetailAPIView, CommentAPIView, CommentDetailAPIView, SubscribeAPIView, TagAPIView

app_name = 'api'


urlpatterns = [
    path('recipes/', RecipeAPIView.as_view(), name='recipes_api'),
    path('recipes/<int:pk>/', RecipeDetailAPIView.as_view(), name='recipes_detail_api'),
    path('stories/', StoryAPIView.as_view(), name='stories_api'),
    path('stories/<int:pk>/', StoryDetailAPIView.as_view(), name='stories_detail_api'),
    path('category/', CategoryAPIView.as_view(), name='category_api'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail_api'),    
    path('recipes/<int:pk>/comment/', CommentAPIView.as_view(), name='comment_api'),
    path('recipes/comment/<int:pk>/', CommentDetailAPIView.as_view(), name='comment_detail_api'),    
    path('subscribe/', SubscribeAPIView.as_view(), name='subscribe'),
    path('tags/', TagAPIView.as_view(), name='tags')
] 