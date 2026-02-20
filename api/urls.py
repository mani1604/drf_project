from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students', views.StudentsView)

urlpatterns = [
    path("teachers/", views.teachers_api_view),
    path("teacher/<int:pk>/", views.teacher_detail),
    path("", include(router.urls)),
    path("mentors/", views.MentorsView.as_view()),
    path("mentors/<str:pk>", views.MentorDetails.as_view())
]