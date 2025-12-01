from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    PostUpdateView
)


urlpatterns = [
    #add paths right here
    path("list/", PostListView.as_view(), name='post_list'),
    path("<int:pk>/", PostDetailView.as_view(), name='post_detail'),
    path("new/", PostCreateView.as_view(), name="new_post"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name = "post_delete"),
    path("<int:pk>/update/", PostUpdateView.as_view(), name = "post_update"),
]