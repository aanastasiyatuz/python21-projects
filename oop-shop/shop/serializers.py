from abstract.serializers import BaseSerializer

from .models import Category, Product, Comment

class CategorySerializer(BaseSerializer):
    class Meta:
        fields = ["title"]
        queryset = Category.objects

class ProductSerializer(BaseSerializer):
    class Meta:
        fields = ["id","title", "price", "desc", "quantity", "category"]
        queryset = Product.objects
    
    def serialize_obj(self, obj):
        dict_ = super().serialize_obj(obj)
        dict_["category"] = obj.category.title
        return dict_

class CommentSerializer(BaseSerializer):
    class Meta:
        fields = ["body", "created_at"]
        queryset = Comment.objects
