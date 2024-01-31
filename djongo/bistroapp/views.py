from rest_framework import generics
from bistroapp.models import Dish
from bistroapp.serializers import DishSerializer


class DishList(generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class DishDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = Dish


