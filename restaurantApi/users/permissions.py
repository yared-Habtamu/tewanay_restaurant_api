from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'ADMIN'


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['MANAGER', 'ADMIN']


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'CUSTOMER'
