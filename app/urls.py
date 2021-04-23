from django.urls import path
from app import views

# 投稿一覧を表示する/投稿詳細を表示する
urlpatterns = [
    path('post/', views.PostView.as_view(), name='post'),
    path('post/<str:pk>/', views.PostDetailView.as_view(), name='post-detail'),
]
