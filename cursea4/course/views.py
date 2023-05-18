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
    if request.method == 'POST':
        course_json = json.loads(request.body)['course_json']
        update_course_from_json(course_json)
        return JsonResponse({'status': 'success', 'message': 'Course updated successfully.'})
    else:
        course = get_object_or_404(Course, title=title)

        return render(request, 'course/edit.html', {'course': course, 'courseJSON': course_detail(course)})


@login_required
def DeleteView(request, title):
    course = get_object_or_404(Course, title=title)
    course.delete()
    return redirect('/course/')


@login_required
def NewCourseView(request):
    course = Course.objects.create(title='Новый курс', visible=False)
    return redirect('/course/' + str(course.title) + '/edit')


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


def update_course_from_json(course_dict):
    course_dict = json.loads(course_dict)
    print(course_dict['id'])
    course_id = course_dict['id']
    course = Course.objects.get(id=course_id)

    # Update course fields
    course.title = course_dict['title']
    course.cover = course_dict['cover']
    course.visible = course_dict['visible']
    course.save()

    # Update or create blocks and items
    for block_dict in course_dict['blocks']:
        block_title = block_dict['title']
        block_order = block_dict['order']
        block, _ = Block.objects.get_or_create(course=course, title=block_title, order=block_order)

        for item_dict in block_dict['items']:
            item_order = item_dict['order']
            item_type = item_dict['type']
            item_name = item_dict['name']
            item_link = item_dict['link']
            item, _ = Item.objects.get_or_create(block=block, order=item_order, type=item_type)
            item.name = item_name
            item.link = item_link
            item.save()
