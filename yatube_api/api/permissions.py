from rest_framework import permissions


class IsAuthorOrCreateReadOnly(permissions.BasePermission):
    """
    Класс для выдачи разрешений:
     - для неавторизованных пользователей доступны только безопасные методы;
     - для авторизованных доступны безопасные методы и создание объекта;
     - для авторов объекта доступны все запросы, в т.ч на изменение и удаление.
    """

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
