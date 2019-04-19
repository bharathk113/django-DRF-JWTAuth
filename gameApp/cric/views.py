from rest_framework import generics
from .models import Newsfeed
from .serializers import PostsSerializer
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

class LargeResultsSetPagination(LimitOffsetPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 8
    default_limit=8

class ListPostsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    permission_classes = (IsAuthenticated,)
    #queryset = Posts.objects.all()
    filter_backends = ()
    queryset=Newsfeed.objects.order_by('-newsid', 'timestamp')[:200]
    serializer_class = PostsSerializer
    pagination_class =LargeResultsSetPagination# LimitOffsetPaginatio
