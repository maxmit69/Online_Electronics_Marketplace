from rest_framework import permissions


class IsActiveUser(permissions.BasePermission):
    """ Права только для активных пользователей """
    def has_permission(self, request, view):
        return request.user and request.user.is_active
