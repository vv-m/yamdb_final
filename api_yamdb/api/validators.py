from django.utils import timezone
from django.core.exceptions import ValidationError


def validate_year(value):
    """Проверка на использование правильной даты"""

    year = timezone.now().year
    if value > year:
        raise ValidationError(
            '{year} еще не наступил :)'
        )
