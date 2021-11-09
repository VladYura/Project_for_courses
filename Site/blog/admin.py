from django.contrib import admin
from .models import News, Reviews, Works, Language, Feedback


admin.site.register(News)  # Регистрация модели Новостей
admin.site.register(Reviews)  # Регистрация модели отзывов о статьях
admin.site.register(Works)  # Регистрация модели о работе
admin.site.register(Language)  # Регистрация модели языков
admin.site.register(Feedback)  # Регистрация модели отзывов о работе
