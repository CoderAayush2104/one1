from rest_framework import permissions

class UpdateOwnUserInfo(permissions.BasePermission):
    """Allow users to eddit their own user info"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own user info"""

        if request.method in permissions.SAFE_METHODS:
            """Allows users to view data but not edit"""
            return True

        return obj.id == request.user.id
