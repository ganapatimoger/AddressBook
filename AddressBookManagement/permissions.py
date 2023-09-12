from rest_framework.permissions import BasePermission

class UserAddressPermission(BasePermission):
    """Permission class for Language crud API"""

    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user