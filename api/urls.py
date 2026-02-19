from django.urls import path
from . import views

urlpatterns = [
    path("teachers/", views.teachers_api_view),
    path("teacher/<int:pk>/", views.teacher_detail),
    path("students/", views.StudentsView.as_view()),
    path("students", views.StudentsView.as_view()), # class based view
    path("student/<int:pk>", views.StudentDetail.as_view())
]