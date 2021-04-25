from django.urls import path

from .views import CourseAPIDetailView, CourseAPIListView

urlpatterns = [
    path('', CourseAPIListView.as_view(), name='course_api_list'),
    path('<int:pk>/', CourseAPIDetailView.as_view(), name='course_api_detail')
    ]
