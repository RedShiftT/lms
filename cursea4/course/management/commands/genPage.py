from django.core.management import BaseCommand
from course.models import Course, Block, Item


class Command(BaseCommand):
    def handle(self, *args, **options):
        course = Course.objects.create(title='Схемотехника', cover='/static/resources/images/1.jpg')

        block = Block.objects.create(course=course, title='Видеоуроки')
        content = ['https://www.youtube.com/watch?v=9IKzf6Medww',
                   'https://www.youtube.com/watch?v=pkt_uw5yZio',
                   'https://www.youtube.com/watch?v=KZYNf211CA8',
                   'https://www.youtube.com/watch?v=Oo5LPEWOQQM',
                   'https://www.youtube.com/watch?v=2fjrLe3X5EE',
                   ]
        for i in content:
            Item.objects.create(block=block, type='youtube', link=i)


        block = Block.objects.create(course=course, title='Учебник')
        for i in range(1, 9):
            Item.objects.create(block=block, type='pdf', name=f'Лекция {i}.', link=f'/static/resources/doc/Lektsia_{i}.pdf')



        course = Course.objects.create(title='Мидовый пудж', cover='/static/resources/images/2.jpg')
        block = Block.objects.create(course=course, title='Гайды')
        content = [
            'https://www.youtube.com/watch?v=v8W7xePn9iQ',
            'https://www.youtube.com/watch?v=rR1mSCEdL4o',
            'https://www.youtube.com/watch?v=A9X02callgQ',
            'https://www.youtube.com/watch?v=J7a4cHW2Z4k',
            'https://www.youtube.com/watch?v=su4FRmZhpok',
            'https://www.youtube.com/watch?v=3oYhzIu3D-o',
        ]
        for i in content:
            Item.objects.create(block=block, type='youtube', link=i)



        course = Course.objects.create(title='EU4 Гайд на Англию', cover='/static/resources/images/2.jpg')
        block = Block.objects.create(course=course, title='Чем сильна Англия?')
        Item.objects.create(block=block, type='text', name="Англия - одна из самых опасных и сильных государств в Европке. У Англии одна из самых лучших форм правления: Английская монархия - представляет из себя смесь парламента с монархией, ее плюсы в том, что она включает в себя парламентские выборы, да и к тому же хорошие статы")
        Item.objects.create(block=block, type='text', name="Английская монархия:\n -Национальные беспорядки: -1.00\nГодовое изменение легитимности: +0.50\nМаксимум абсолютизма: -30.00\nЛимит управления: +50")




