from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('',views.PostList.as_view(),name='list'),
    path('create/',views.PostCreate.as_view(),name='create'),
    
]