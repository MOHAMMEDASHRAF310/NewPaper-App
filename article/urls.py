from django.urls import path
from .views import ArticleListView , articledetailsview,articledelete,articleEdit ,createnewarticle
urlpatterns=[
    path('<int:pk>/',articledetailsview.as_view(),name='article_derials'),
    path('<int:pk>/edit',articleEdit.as_view(),name='article_Edit'),
    path('<int:pk>/delete',articledelete.as_view(),name='article_delete'),
    path('',ArticleListView.as_view(),name='article_view'),
    path('new/',createnewarticle.as_view(),name='new_view')
]