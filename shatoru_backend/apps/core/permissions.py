from rest_framework.permissions import BasePermission


class IsDriverOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.is_active
            and request.user.groups.filter(name="Driver").exists()
        )
