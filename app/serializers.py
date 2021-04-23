# クエリセットやモデルインスタンスのような複雑なデータをJSON形式に変換する

from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    # 見やすいフォーマットに整形
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = Post
        fields = ('id', 'title', 'image', 'content', 'created_at')
