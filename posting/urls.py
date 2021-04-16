from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverView, name="api-overview"),
    path('post-by-sub/<pk>', views.postList, name="post-by-subject"),
    path('create-post', views.create_post, name="post-create"),
    path('update-post/<pk>', views.update_post, name="post-update"),
    path('delete/<pk>', views.delete_post, name="post-delete"),
    path('user-post', views.user_posts, name="user-post")
]