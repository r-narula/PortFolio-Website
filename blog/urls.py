from django.urls import path
from . import views
from .views import PostView
urlpatterns = [
    path('',views.home,name='blog-home'),
    path('about/',views.about,name='blog-about'),
    path('<int:pk>/',PostView.as_view(),name='blog-mapper'),
]
