# Generated by Django 4.2.11 on 2024-03-20 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0011_remove_room_excerpt_remove_room_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='owner_email',
            field=models.EmailField(max_length=200, unique=True),
        ),
    ]
