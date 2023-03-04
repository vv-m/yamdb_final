from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Права доступа для автора или только для чтения"""

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            or request.user.is_admin
            or request.user.is_moderator
            or request.user.is_superuser
        )


class IsAdminOrReadOnly(permissions.BasePermission):
    """Права доступа для админа или только для чтения"""

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
                and (request.user.is_admin or request.user.is_superuser))

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
                and (request.user.is_admin or request.user.is_superuser))


class IsSuperUserOrAdmin(permissions.BasePermission):
    """Права доступа для админа или суперпользователя"""

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and (request.user.is_superuser
                 or request.user.is_staff
                 or request.user.is_admin)
        )

    def has_object_permission(self, request, view, obj):
        return (request.user.is_authenticated
                and (request.user.is_superuser
                     or request.user.is_staff
                     or request.user.is_admin))
