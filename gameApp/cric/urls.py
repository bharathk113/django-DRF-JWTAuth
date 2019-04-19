from django.urls import path
from .views import ListPostsView


urlpatterns = [
    path('cric/', ListPostsView.as_view(), name="posts-all")
]
