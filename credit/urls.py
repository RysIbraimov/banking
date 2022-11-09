from django.urls import path
from .views import DetailClientView,ClientViews

urlpatterns = [
    path('',ClientViews.as_view(),name='clients'),
    path('detail/<int:pk>/', DetailClientView.as_view(), name='detail')
]