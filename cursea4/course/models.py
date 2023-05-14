from django.db import models
import re
import urllib.request


def get_video_title(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    title = re.findall("<title>(.+?)</title>", html.decode("utf-8"))[0]
    return title[:-10]


class Course(models.Model):
    title = models.CharField(max_length=255, unique=True)
    cover = models.ImageField(upload_to='static/resources/images', default='static/resources/images/Нет картинки.jpg')


class Block(models.Model):
    title = models.CharField(max_length=255, default=None)
    course = models.ForeignKey(Course, related_name='blocks', on_delete=models.CASCADE, default=None)
    order = models.PositiveIntegerField(default=0)


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
