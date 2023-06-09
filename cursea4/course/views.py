
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from .models import Course, Block, Item
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.core import serializers
import json
from django.http import HttpResponse

@login_required
def CourseView(request, title):
    course = get_object_or_404(Course, title=title)

    if (request.user.group.first() in course.groups.all()) or (request.user in course.lector.all()):
        return render(request, 'course/course.html', {'course': course})
    else:
        return HttpResponse('403')

@staff_member_required
@user_passes_test(lambda u: u.groups.filter(name='lector').exists())
def EditView(request, title):
    if request.method == 'POST':
        course_json = json.loads(request.body)
        print(course_json)
        update_course_from_json(course_json)
        return JsonResponse({'status': 'success', 'message': 'Course updated successfully.'})
    else:
        course = get_object_or_404(Course, title=title)
        print(cd := course_detail(course))
        return render(request, 'course/edit.html', {'course': course, 'courseJSON': cd})


@staff_member_required
def DeleteView(request, title):
    course = get_object_or_404(Course, title=title)
    course.delete()
    return redirect('/course/')


@staff_member_required
def NewCourseView(request):
    course = Course.objects.create(title='Новый курс', hidden=True)
    return redirect('/course/' + str(course.title) + '/edit')


@login_required
def AllСourseView(request):
    query = request.GET.get('q')

    if query:
        courses = Course.objects.filter(title__icontains=query)
    else:
        courses = Course.objects.all()

    gr = request.user.group.first()
    if gr:
        if gr.name == 'lector':
            courses = Course.objects.filter(lector=request.user)
        else:
            courses = courses.filter(groups__name=gr)

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
    print(course_dict['id'])
    course_id = course_dict['id']
    course = Course.objects.get(id=course_id)

    course.title = course_dict['title']
    course.cover = course_dict['cover']
    course.hidden = course_dict['hidden']
    course.save()

    block_ids = []
    item_ids = []

    for block_dict in course_dict['blocks']:
        print(block_dict['title'])
        block_title = block_dict['title']
        block_order = block_dict['order']
        block, _ = Block.objects.get_or_create(course=course, title=block_title, order=block_order)
        block_ids.append(block.id)

        for item_dict in block_dict['items']:
            item_order = item_dict['order']
            item_type = item_dict['type']
            item_name = item_dict['name']
            item_link = item_dict['link']
            item, _ = Item.objects.get_or_create(block=block, order=item_order, type=item_type)
            item.name = item_name
            item.link = item_link
            item.save()
            item_ids.append(item.id)

    Block.objects.filter(course=course).exclude(id__in=block_ids).delete()
    Item.objects.filter(block__course=course).exclude(id__in=item_ids).delete()