from rest_framework import serializers, generics
from bistroapp.models import Dish

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['name', 'description', 'price']
