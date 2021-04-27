from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, CommentCreateView

app_name = 'posts'
urlpatterns = [
    path('blog/<int:post_pk>/comment',
         CommentCreateView.as_view(), name='comment_new'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name="post_delete"),
    path('blog/<int:pk>/edit/', BlogUpdateView.as_view(), name="post_edit"),
    path('blog/new/', BlogCreateView.as_view(), name="post_new"),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name="post_detail"),
    path('', BlogListView.as_view(), name="home"),
    path('blog/', BlogListView.as_view(), name="home"),
]
