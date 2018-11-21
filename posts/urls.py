from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('',views.PostList.as_view(),name='list'),
    path('create/',views.PostCreate.as_view(),name='create'),
    path('by/<username>/<pk>/',views.PostDetail.as_view(),name='detail'),
    path('by/<username>/',views.UserPosts.as_view(),name="for_user"),
    path('delete/<pk>/',views.PostDelete.as_view(),name='delete'),
    path('update/<pk>/',views.PostUpdate.as_view(),name='update'),
    
]