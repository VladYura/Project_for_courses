from django.db import models
from datetime import date
from django.urls import reverse


# Модель для новостей
class News(models.Model):
    """Новости"""
    title = models.CharField("Заголовок", max_length=150)
    name = models.CharField("Автор", max_length=100)
    description = models.TextField("Описание")
    text = models.TextField("Текст новости")
    date = models.DateField("Дата публикации", default=date.today)
    url = models.SlugField(max_length=160, unique=True)

    # Функция, возвращающая url новости
    def get_absolute_url(self):
        return reverse('single', kwargs={'slug': self.url})

    def __str__(self):
        return self.title

    # Метаданные
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


# Модель для отзывов
class Reviews(models.Model):
    """Отзывы"""
    name = models.CharField("Имя", max_length=100)
    email = models.EmailField()
    text = models.TextField("Сообщение", max_length=5000)
    news = models.ForeignKey(News, verbose_name="Новость", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.news}"

    # Метаданные
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


# Модель для языков
class Language(models.Model):
    """Языки программирования"""
    name = models.CharField('Название языка', max_length=50)

    def __str__(self):
        return self.name

    # Метаданные
    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'


# Модель для работ
class Works(models.Model):
    """Мои работы"""
    name = models.CharField("Название", max_length=50)
    skills = models.ForeignKey(Language, verbose_name='Язык программирования', on_delete=models.CASCADE)
    duration = models.CharField("Количество затраченного времени", max_length=10)
    url = models.CharField('Url', max_length=160)
    about = models.CharField("О проекте", max_length=150)
    image = models.ImageField('Картинка', upload_to='works/', default='static/images/default.jpg')

    def __str__(self):
        return self.name

    # Метаданные
    class Meta:
        verbose_name = 'Моя работа'
        verbose_name_plural = 'Мои работы'


# Модель для отзывов о работе
class Feedback(models.Model):
    """Отзывы о работе"""
    name = models.CharField("Имя", max_length=50)
    email = models.EmailField()
    text = models.TextField("Отзыв", max_length=150)
    work = models.CharField("Место работы", max_length=50)

    def __str__(self):
        return self.name

    # Метаданные
    class Meta:
        verbose_name = "Отзыв о работе"
        verbose_name_plural = "Отзывы о работе"
