from django.contrib.auth.models import User, Group
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import serializers

from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import (
    CategorySerializer,
    MenuItemSerializer,
    CartSerializer,
    OrderSerializer
)
from .permissions import IsManager, IsDeliveryCrew, IsAdminOrManager, IsAdminOrManagerOrDelivery


# CATEGORY VIEWS

class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


# MENU ITEM VIEWS

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [AllowAny]

    filter_backends = [OrderingFilter, SearchFilter]

    ordering_fields = ['price']
    search_fields = ['category__title']

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), IsAdminOrManager()]
        return [AllowAny()]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated(), IsAdminOrManager()]
        return [AllowAny()]


# MANAGER GROUP

class ManagersView(APIView):

    permission_classes = [IsAuthenticated, IsAdminOrManager]

    def get(self, request):
        managers = User.objects.filter(groups__name='Manager')
        data = [{'id': user.id, 'username': user.username} for user in managers]
        return Response(data)

    def post(self, request):
        username = request.data.get('username')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(
                {'error': 'User not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        manager_group, _ = Group.objects.get_or_create(name='Manager')
        manager_group.user_set.add(user)

        return Response({'message': 'User added to Manager group'})


# DELIVERY CREW GROUP

class DeliveryCrewView(APIView):

    permission_classes = [IsAuthenticated, IsAdminOrManager]

    def get(self, request):
        crew = User.objects.filter(groups__name='Delivery crew')
        data = [{'id': user.id, 'username': user.username} for user in crew]
        return Response(data)

    def post(self, request):
        username = request.data.get('username')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(
                {'error': 'User not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        crew_group, _ = Group.objects.get_or_create(name='Delivery crew')
        crew_group.user_set.add(user)

        return Response({'message': 'User added to Delivery Crew'})


# CART

class CartView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Use validated data instead of raw request data
        validated = serializer.validated_data
        menuitem_id = validated.get('menuitem_id')
        quantity = validated.get('quantity')

        try:
            menuitem = MenuItem.objects.get(id=menuitem_id)
        except MenuItem.DoesNotExist:
            raise serializers.ValidationError({'menuitem_id': 'Invalid menuitem_id'})

        serializer.save(
            user=self.request.user,
            menuitem=menuitem,
            quantity=quantity,
            unit_price=menuitem.price,
            price=menuitem.price * quantity
        )

    def delete(self, request):
        Cart.objects.filter(user=request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ORDERS

class OrderView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        if self.request.user.groups.filter(name='Manager').exists() or self.request.user.is_staff:
            return Order.objects.all()

        if self.request.user.groups.filter(name='Delivery crew').exists():
            return Order.objects.filter(delivery_crew=self.request.user)

        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):

        cart_items = Cart.objects.filter(user=self.request.user)

        if not cart_items.exists():
            from rest_framework.exceptions import ValidationError
            raise ValidationError({'detail': 'Cart is empty'})

        total = sum(item.price for item in cart_items)

        order = serializer.save(
            user=self.request.user,
            total=total
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                menuitem=item.menuitem,
                quantity=item.quantity,
                unit_price=item.unit_price,
                price=item.price
            )

        cart_items.delete()


class SingleOrderView(generics.RetrieveUpdateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        if self.request.user.groups.filter(name='Manager').exists() or self.request.user.is_staff:
            return Order.objects.all()

        if self.request.user.groups.filter(name='Delivery crew').exists():
            return Order.objects.filter(delivery_crew=self.request.user)

        return Order.objects.filter(user=self.request.user)

    def get_permissions(self):
        # For updates (assigning delivery crew, marking delivered) allow manager, delivery crew, or admin
        if self.request.method in ['PUT', 'PATCH']:
            return [IsAuthenticated(), IsAdminOrManagerOrDelivery()]
        return [IsAuthenticated()]