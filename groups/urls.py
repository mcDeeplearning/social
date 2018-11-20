from django.urls import path
from . import views
app_name = 'groups'

urlpatterns = [
    path('',views.GroupList.as_view(),name='list'),
    path('create/',views.GroupCreate.as_view(),name="create"),
]