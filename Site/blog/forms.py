from django import forms

from .models import Reviews, Feedback


# Класс формы отзывов о статье
class ReviewForm(forms.ModelForm):
    """Форма отзывов"""
    class Meta:
        model = Reviews  # Модель, от которой строится форма
        fields = ('name', 'email', 'text')  # Требуемые поля из модели


# Класс формы отзывов о работе
class FeedbackForm(forms.ModelForm):
    """Форма отзыва о работе"""
    class Meta:
        model = Feedback  # Модель, от которой строится форма
        fields = ('name', 'email', 'work', 'text')  # Требуемые поля из модели
