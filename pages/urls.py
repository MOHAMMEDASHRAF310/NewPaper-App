from django.urls import path
from .views import Viewhome

urlpatterns=[
    path('',Viewhome.as_view(),name='home')
]