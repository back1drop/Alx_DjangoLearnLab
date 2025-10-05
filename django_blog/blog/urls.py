
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # registration
    path("register/", views.register, name="register"),

    # login and logout using built-in views
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="blog/logout.html"), name="logout"),

    # profile (view & edit)
    path("profile/", views.profile, name="profile"),
       path('posts/<int:pk>/comments/new/', views.add_comment, name='add-comment'),
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment-edit'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('post/<int:post_id>/comment/new/', views.CommentCreateView.as_view(), name='add-comment'),
    path('search/', views.search_posts, name='search-posts'),
    path('tags/<str:tag_name>/', views.posts_by_tag, name='posts-by-tag'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]
