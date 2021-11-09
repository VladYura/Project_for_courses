from django.shortcuts import render, redirect
from django.views.generic.base import View

from .forms import ReviewForm, FeedbackForm
from .models import News, Works, Feedback


# Класс отображения index.html
class BlogView(View):

    def get(self, request):
        news = News.objects.all()
        return render(request, 'index.html', {'news': news})


# Класс отображения about.html
class AboutView(View):

    def get(self, request):
        return render(request, 'about.html')


# Класс отображения contact.html
class ContactView(View):

    def get(self, request):
        feedbacks = Feedback.objects.all()
        return render(request, 'contact.html', {'feedbacks': feedbacks})


# Класс отображения work.html
class SingleView(View):

    def get(self, request, slug):
        news = News.objects.get(url=slug)
        return render(request, 'single.html', {"news": news})


# Класс отображения work.html
class WorkView(View):

    def get(self, request):
        works = Works.objects.all()
        return render(request, 'work.html', {'works': works})


# Класс для отправки отзывов о статье
class AddReview(View):

    def post(self, request, pk):
        form = ReviewForm(request.POST)  # Заполнение формы из формы на сайте
        new = News.objects.get(id=pk)  # Из модели берём статью по id
        if form.is_valid():  # Проверка на валидность
            form = form.save(commit=False)  # Приостановка сохранения формы
            form.news = new  # Указываем статью, к которой нужно привязаться
            form.save()  # Заносим данные в базу
        return redirect(new.get_absolute_url())  # Перенаправление обратно на статью


# Класс для отправки отзывов о работе
class AddFeedback(View):

    def post(self, request):
        form = FeedbackForm(request.POST)  # Заполнение формы из формы на сайте
        if form.is_valid():  # Проверка на валидность
            form = form.save(commit=False)  # Приостановка сохранения формы
            form.save()  # Заносим данные в базу
        return redirect('contact')  # Перенаправление на обратно на contact.html

