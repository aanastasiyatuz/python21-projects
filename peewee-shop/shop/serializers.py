from abstract.serializers import BaseSerializer
from .models import Product, Comment

class ProductSerializer(BaseSerializer):
    class Meta:
        fields = ("id", "category", "title", "price", "description", "comments")
        model = Product
    
    def serialize_obj(self, obj):
        product = super().serialize_obj(obj)
        product["comments"] = CommentSerializer().serialize_queryset(obj.comments)
        return product

class CommentSerializer(BaseSerializer):
    class Meta:
        fields = ("id", "user", "body", "created_at")
        model = Comment

    def serialize_obj(self, obj):
        comment = super().serialize_obj(obj)
        comment["user"] = obj.user.username
        return comment