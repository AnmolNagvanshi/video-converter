from django.urls import path

from . import views


urlpatterns = [
    path('videos/<int:pk>/', views.VideoDetail.as_view(), name='video-detail'),
    path('videos/', views.FileUploadView.as_view(), name='video-upload'),
    path('videos/celerydemo', views.CeleryDemo.as_view(), name='video-celery-demo')
]

