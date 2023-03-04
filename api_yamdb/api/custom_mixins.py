from rest_framework import mixins, viewsets


class CategoryGenreViewSet(viewsets.GenericViewSet,
                           mixins.ListModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.CreateModelMixin):
    """CRUD для моделей Genre и Category"""
    pass
