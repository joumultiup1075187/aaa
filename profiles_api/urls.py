from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views

# ////creating viewset URL///////////////////////////////////
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

urlpatterns =[
    path("hello-view/", views.HelloApiView.as_view()),
    # registering viewset URLs
    path('', include(router.urls))
]