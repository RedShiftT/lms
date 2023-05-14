import os

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



        names = [
            "Молекулярная генетика и биотехнология",
            "Радиофизика и электроника полупроводников",
            "Компьютерное зрение и обработка изображений",
            "Функциональный анализ и теория операторов",
            "Теория и практика параллельных вычислений",
            "Сложность вычислений и теория алгоритмов",
            "Искусственный интеллект и машинное обучение",
            "Теория управления и оптимальное управление",
            "Сетевые протоколы и технологии интернета вещей",
            "Биомедицинская оптика и фотоника",
            "Распознавание речи и естественный язык",
            "Современные технологии производства электроники",
            "Теория и практика тестирования программного обеспечения",
            "Геномика и биоинформатика",
            "Криптография и информационная безопасность",
            "Системы автоматического управления транспортом",
            "Нанотехнологии и наноматериалы",
            "Численные методы и математическое моделирование",
            "Разработка и тестирование мобильных приложений",
            "Геоинформационные системы и технологии",
            "Микроэлектроника и микросистемы",
            "Анализ данных и статистическое моделирование",
            "Теория информации и кодирование",
            "Моделирование и управление производственными процессами",
            "Интеллектуальные системы и технологии",
            "Фотоника и лазерные технологии",
            "Системы технического зрения и робототехника",
            "Биоорганическая химия и биоматериалы",
            "Технологии виртуальной и дополненной реальности",
            "Технологии энергосбережения и экологически чистые технологии",
        ]

        for n in names:
            course = Course.objects.create(title=n,
                                           cover=f'/static/resources/images/{n}.jpg'
                                           if os.path.isfile(fr'C:/Users/RedShifT/PycharmProjects/pythonProject/cursea4/static/resources/images/{n}.jpg')
                                           else 'static/resources/images/Нет картинки.jpg')


