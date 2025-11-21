from rest_framework.permissions import BasePermission



class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):

        print(f"Request user: {request.user}, Object owner: {obj.owner}")
        return obj.owner.id == request.user.id


