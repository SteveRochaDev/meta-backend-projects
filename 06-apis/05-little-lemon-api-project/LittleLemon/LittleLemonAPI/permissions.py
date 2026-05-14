from rest_framework.permissions import BasePermission


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.groups.filter(name='Manager').exists()


class IsDeliveryCrew(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.groups.filter(name='Delivery crew').exists()


class IsAdminOrManager(BasePermission):
    """Allow access if user is staff (admin) or in Manager group."""

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        if user.is_staff or user.is_superuser:
            return True
        return user.groups.filter(name='Manager').exists()


class IsAdminOrManagerOrDelivery(BasePermission):
    """Allow if staff/superuser, manager, or delivery crew."""

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        if user.is_staff or user.is_superuser:
            return True
        if user.groups.filter(name='Manager').exists():
            return True
        if user.groups.filter(name='Delivery crew').exists():
            return True
        return False