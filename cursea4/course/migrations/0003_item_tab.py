# Generated by Django 4.2 on 2023-05-07 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_block_course_alter_item_block_alter_item_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='tab',
            field=models.BooleanField(default=False),
        ),
    ]
