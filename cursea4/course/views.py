from django.db.models import Prefetch
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.db.models import Q
from .models import Course, Block, Item
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from django.template.loader import render_to_string
from django.http import JsonResponse


@login_required
def CourseView(request, title):
    course = get_object_or_404(Course, title=title)
    return render(request, 'course/course.html', {'course': course})



@login_required
def AllСourseView(request):
    query = request.GET.get('q')

    if query:
        courses = Course.objects.filter(title__icontains=query)
    else:
        courses = Course.objects.all()


    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('course/cards.html', {'courses': courses})
        return JsonResponse({'html': html})

    return render(request, 'course/all.html', {"courses": courses})

