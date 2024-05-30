from rest_framework import mixins, viewsets


class ListOrCreateViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    """
    Базовый класс-вьюсет, который предоставляет методы `create()` и `list()`.
    """
