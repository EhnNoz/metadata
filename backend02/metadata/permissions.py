from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """Allow owners to read/write their own records; admin all."""

    def has_object_permission(self, request, view, obj):
        # Superusers have full access
        if request.user and request.user.is_superuser:
            return True

        # For unsafe methods, deny deletion if final_status is True
        if view.action == 'destroy' and getattr(obj, 'final_status', False):
            return False

        # Owners can CRUD except controlled fields
        return obj.owner == request.user


class AdminWriteRestrictedFields(permissions.BasePermission):
    """Prevent non-superusers from setting admin-only fields."""

    def has_permission(self, request, view):
        # Only applies to create and update
        if view.action in ['create', 'update', 'partial_update']:
            # If any admin-only fields in request data and user is not superuser
            forbidden = {'final_status', 'base_code', 'father_code'}
            if not request.user.is_superuser:
                if forbidden.intersection(request.data.keys()):
                    return False
        return True