# Generated by Django 3.2.8 on 2021-11-05 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_language_works'),
    ]

    operations = [
        migrations.AddField(
            model_name='works',
            name='image',
            field=models.ImageField(default='static/images/default.jpg', upload_to='works/', verbose_name='Картинка'),
        ),
    ]
