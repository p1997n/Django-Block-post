
from django.urls import path
from .views import HomeView, AddPost, UpdatePost, DeletePost

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('addPost/',AddPost.as_view(),name="add_post"),
    path('updatePost/<int:pk>',UpdatePost.as_view(),name="update_post"),
    path('<int:pk>/remove',DeletePost.as_view(),name="delete_post"),
]