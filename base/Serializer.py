from rest_framework import serializers
from .models import Category, Order, OrderDetails, Product
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'order_date']
        read_only_fields = ['user', 'order_date']

    def create(self, validated_data):
        # Retrieve the user from the context
        user = self.context['request'].user

        # Add the user to the validated data before creating the order
        validated_data['user'] = user

        # Create and return the order
        order = Order.objects.create(**validated_data)
        return order

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom columns (user return payload - when login)
        token['username'] = user.username
        token['emaillll'] = user.email
        token['blabla'] = "waga baga bbb"
        # ...
        return token