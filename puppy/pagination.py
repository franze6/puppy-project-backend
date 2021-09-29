from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'page_params': {
                'page_count': self.page.paginator.num_pages if self.page.paginator.count != 0 else 0,
                'record_count': self.page.paginator.count,
                'default_page_size': self.page_size,
                'max_page_size': self.max_page_size,
            },
            'results': data
        })