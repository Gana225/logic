from rest_framework import serializers
from .models import FoodItem,Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class FoodItemsSerializer(serializers.ModelSerializer):
    image = serializers.CharField(source='image.url', read_only=True)
    category = CategorySerializer()

    class Meta:
        model = FoodItem
        fields = "__all__"



