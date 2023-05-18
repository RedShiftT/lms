from django.db import models
import re
import urllib.request

from accounts.models import CustomGroup


def get_video_title(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    title = re.findall("<title>(.+?)</title>", html.decode("utf-8"))[0]
    return title[:-10]


class Course(models.Model):
    title = models.CharField(max_length=255, unique=True)
    cover = models.ImageField(upload_to='static/resources/images', default='static/resources/images/Нет картинки.jpg')
    hidden = models.BooleanField(default=True)
    groups = models.ManyToManyField(CustomGroup, blank=True)

    def save(self, *args, **kwargs):
        # Check if the course name already exists
        if Course.objects.filter(title=self.title).exists():
            # Append a number to the course name
            i = 2
            while Course.objects.filter(title=f'{self.title} {i}').exists():
                i += 1
            self.title = f'{self.title} {i}'

        super().save(*args, **kwargs)

class Block(models.Model):
    title = models.CharField(max_length=255, default=None)
    course = models.ForeignKey(Course, related_name='blocks', on_delete=models.CASCADE, default=None)
    order = models.PositiveIntegerField(default=0)
    hidden = models.BooleanField(default=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.order:
            max_order_item = Block.objects.filter(course=self.course).order_by('-order').first()
            self.order = max_order_item.order + 1 if max_order_item else 1


class Item(models.Model):
    BLOCK_ITEM_CHOICES = [
        ('text', 'Text'),
        ('header', 'Header'),
        ('pdf', 'pdf'),
        ('video', 'Video'),
        ('image', 'Image'),
        ('link', 'Link'),
        ('youtube', 'Youtube'),
    ]
    block = models.ForeignKey(Block, related_name='items', on_delete=models.CASCADE, default=None)
    order = models.PositiveIntegerField(default=0)

    type = models.CharField(max_length=10, choices=BLOCK_ITEM_CHOICES)

    name = models.CharField(max_length=100, default="")
    link = models.URLField(default="")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.type == 'youtube':
            self.name = get_video_title(self.link)

        if not self.order:
            max_order_item = Item.objects.filter(block=self.block).order_by('-order').first()
            self.order = max_order_item.order + 1 if max_order_item else 1
