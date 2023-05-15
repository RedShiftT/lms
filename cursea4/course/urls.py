from django.urls import path
from . import views
from .views import CourseView, AllСourseView

app_name = 'course'

urlpatterns = [
    path('', AllСourseView, name='all_courses'),




    path('<str:title>', CourseView, name='1'),

]