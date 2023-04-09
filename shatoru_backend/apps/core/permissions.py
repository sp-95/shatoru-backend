from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.request import Request
from rest_framework.views import View


class IsDriverOwner(BasePermission):
    """
    Permission class that checks if the user is authenticated, active and belongs to the
    Driver group, and if the user is the owner of the requested object.

    Methods:
        has_permission(request, view): Returns True if the user is authenticated, active
            and belongs to the Driver group.
        has_object_permission(request, view, obj): Returns True if the requested object
            belongs to the authenticated user.
    """

    def has_permission(self, request: Request, view: View) -> bool:
        """
        Returns True if the user is authenticated, active and belongs to the Driver
        group.

        Args:
            request (Request): The request object.
            view (View): The view object.

        Returns:
            bool: True if the user is authenticated, active and belongs to the Driver
                group.
        """
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.is_active
            and request.user.groups.filter(name="Driver").exists(),
        )

    def has_object_permission(self, request: Request, view: View, obj) -> bool:
        """
        Returns True if the requested object belongs to the authenticated user.

        Args:
            request (Request): The request object.
            view (View): The view object.
            obj (object): The object to check permissions against.

        Returns:
            bool: True if the requested object belongs to the authenticated user.
        """
        return obj.id == request.user.id


class IsAdminOrReadOnly(BasePermission):
    """
    Permission class that checks if the user is a superuser or if the request method is
    one of the safe methods.

    Methods:
        has_permission(request, view): Returns True if the user is a superuser or if the
            request method is one of the safe methods.
    """

    def has_permission(self, request: Request, view: View) -> bool:
        """
        Returns True if the user is a superuser or if the request method is one of the
        safe methods.

        Args:
            request (Request): The request object.
            view (View): The view object.

        Returns:
            bool: True if the user is a superuser or if the request method is one of the
                safe methods.
        """
        return bool(
            request.method in SAFE_METHODS
            or request.user
            and request.user.is_superuser,
        )
