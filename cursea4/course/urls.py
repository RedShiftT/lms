from django.urls import path
from . import views
from .views import courseview, allcoursesview

app_name = 'course'

urlpatterns = [
    path('', allcoursesview, name='all_courses'),
    path('<str:title>', courseview, name='1'),
]