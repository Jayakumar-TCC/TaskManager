from django.urls import path
from . import views
urlpatterns = [
    path("students/",views.studentsView),
    path("students/<int:pk>/",views.studentDetailView),

    path("employee/<int:pk>/",views.EmployeeDetail.as_view())
]