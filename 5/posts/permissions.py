from rest_framework import permissions
# object-level permission


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # read only are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permission for only author
        return obj.author == request.user
