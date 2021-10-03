from django.urls import path

from . import views

urlpatterns = [
    path('users/<username>/collection', views.MicropostsListView.as_view(),
         name='user-collection'),
    path('users/<username>/collection/<pk>', views.MicropostView.as_view(),
         name='micropost-detail'),
]
