from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True

        if request.method in SAFE_METHODS:
            return True if request.user and request.user.is_authenticated else False

        is_order_endpoint = getattr(view, "basename", None) == "order" or getattr(view, "action", None) == "create"
        if is_order_endpoint and request.method == "POST" and request.user and request.user.is_authenticated:
            return True

        return False
