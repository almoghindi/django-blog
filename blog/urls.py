from django.urls import path

from . import views

urlpatterns = [
    path('', views.StartingPageView.as_view(), name='start-page'),
    path('posts', views.PostsView.as_view(), name='posts'),
    path('page/<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
    path('read-later', views.ReadLaterView.as_view(), name='read-later'),
]
