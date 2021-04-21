from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path(
        '<int:pk>/', views.CourseDetailView.as_view(),
        name='course_detail'
        ),
    path(
        '<int:pk>/update/', views.CourseUpdateView.as_view(),
        name='course_update'
        ),
    path(
        'create/', views.CourseCreateView.as_view(),
        name='course_create'
        ),
    path(
        '<int:pk>/delete/', views.CourseDeleteView.as_view(),
        name='course_delete'
        )
    ]
