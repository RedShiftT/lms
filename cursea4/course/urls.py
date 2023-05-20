from django.urls import path
from .views import CourseView, AllСourseView, EditView, DeleteView, NewCourseView

app_name = 'course'

urlpatterns = [
    path('', AllСourseView, name='all_courses'),
    path('<str:title>/delete', DeleteView, name='delete'),
    path('new', NewCourseView, name='new'),
    path('<str:title>/edit', EditView, name='edit'),
    path('<str:title>', CourseView, name='course'),
]