from rest_framework import viewsets
from .serializers import PostSerializer
from ..models import Post


class PostViewSet(viewsets.ModelViewSet):
    """
    A Simple **POST** API.
    Manage blg posts - create, read, update or delete posts.

    ## Available Endpoints

    - GET/posts/ - List all posts
    - POST/posts/ - Create a new post
    - GET/posts/{id}/ - Retrieve a specific post
    - PUT/posts/{id}/ - Update a specific post
    - DELETE/posts/{id}/ - Delete a specific post
    - PATCH/posts/{id}/ - Partially update a specific post
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
