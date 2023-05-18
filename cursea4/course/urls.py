from django.urls import path
from . import views
from .views import CourseView, AllСourseView, EditView, DeleteView

app_name = 'course'

urlpatterns = [
    path('', AllСourseView, name='all_courses'),
    path('<str:title>/delete', DeleteView, name='delete'),
    path('<str:title>/edit', EditView, name='edit'),
    path('<str:title>', CourseView, name='course'),

]