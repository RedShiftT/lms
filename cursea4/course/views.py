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
from django.core import serializers
import json

@login_required
def CourseView(request, title):
    course = get_object_or_404(Course, title=title)
    return render(request, 'course/course.html', {'course': course})


@login_required
def EditView(request, title):
    course = get_object_or_404(Course, title=title)

    return render(request, 'course/edit.html', {'course': course, 'courseJSON': course_detail(course)})

@login_required
def DeleteView(request, title):
    course = get_object_or_404(Course, title=title)
    course.delete()
    return redirect('/course/')


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


def course_detail(course):
    course_data = serializers.serialize('json', [course])
    course_dict = json.loads(course_data)[0]['fields']
    course_dict['id'] = json.loads(course_data)[0]['pk']
    course_dict['blocks'] = []

    for block in course.blocks.all():
        block_dict = {}
        block_dict['title'] = block.title
        block_dict['order'] = block.order
        block_dict['items'] = []

        for item in block.items.all():
            item_dict = {}
            item_dict['order'] = item.order
            item_dict['type'] = item.type
            item_dict['name'] = item.name
            item_dict['link'] = item.link
            block_dict['items'].append(item_dict)

        course_dict['blocks'].append(block_dict)

    return json.dumps(course_dict)
