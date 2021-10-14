from django.urls import path
from .views import *

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='courses_list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='courses_detail')
]
