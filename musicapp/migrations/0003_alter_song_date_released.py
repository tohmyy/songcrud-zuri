# Generated by Django 4.1.2 on 2022-10-25 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_alter_song_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='date_released',
            field=models.DateField(null=True),
        ),
    ]
