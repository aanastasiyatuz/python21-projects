from abstract.serializers import BaseSerializer

from .models import Category, Product, Comment

class CategorySerializer(BaseSerializer):
    class Meta:
        fields = ["title"]
        queryset = Category.objects

class ProductSerializer(BaseSerializer):
    class Meta:
        fields = ["id","title", "price", "desc", "quantity", "category", "comments", "color"]
        queryset = Product.objects
    
    def serialize_obj(self, obj):
        dict_ = super().serialize_obj(obj)
        dict_["category"] = obj.category.title
        dict_["comments"] = CommentSerializer().serialize_queryset(obj.comments)
        return dict_

class CommentSerializer(BaseSerializer):
    class Meta:
        fields = ["body", "created_at"]
        queryset = Comment.objects
    
    def serialize_obj(self, obj):
        dict_ = super().serialize_obj(obj)
        dict_['user'] = obj.user.email
        dict_['created_at'] = obj.created_at.strftime("%d.%m.%Y %H:%M:%S")
        return dict_