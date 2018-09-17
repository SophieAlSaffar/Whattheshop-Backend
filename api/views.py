from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import UserCreateSerializer
from .models import Product
from .serializers import ProductSerializer

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class ProductAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
