from rest_framework import generics
from .serializers import PostSerializer
from .models import Post

# 投稿一覧を取得


class PostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# 投稿詳細を取得


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
