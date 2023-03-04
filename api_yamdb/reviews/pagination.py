from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class Custom1Pagination(PageNumberPagination):
    """Кастомная пагинация"""
    page_size = 10


class CustomPagination(PageNumberPagination):
    page_size = 10
    """Кастомная пагинация"""

    def get_paginated_response(self, data):
        return Response([{
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        }])
