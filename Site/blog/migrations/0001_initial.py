# Generated by Django 3.2.8 on 2021-10-26 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('name', models.CharField(max_length=100, verbose_name='Автор')),
                ('description', models.TextField(verbose_name='Описание')),
                ('text', models.TextField(verbose_name='Текст новости')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Дата публикации')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
