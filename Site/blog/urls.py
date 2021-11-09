from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogView.as_view(), name='home'),  # Адрес главной страницы
    path('about.html', views.AboutView.as_view(), name='about'),  # Адрес страницы обо мне
    path('contact.html', views.ContactView.as_view(), name='contact'),  # Адрес страницы контактов
    path('<slug:slug>/', views.SingleView.as_view(), name='single'),  # Адрес статьи
    path('work.html', views.WorkView.as_view(), name='work'),  # Адрес страницы о работах
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review'),  # Адреес для отправки формы отзывов о статье
    path('/feedback/', views.AddFeedback.as_view(), name='add_feedback'),  # Адрес для отправки формы отзывов о работе
]