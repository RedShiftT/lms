from django.db.models import Prefetch
from django.shortcuts import render, get_object_or_404
from .models import Course, Block, Item
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def courseview(request, title):
    course = get_object_or_404(Course, title=title)
    return render(request, 'course/course.html', {'course': course})



@login_required
def allcoursesview(request):
    courses = Course.objects.all()
    return render(request, 'course/all.html', {"courses": courses})
