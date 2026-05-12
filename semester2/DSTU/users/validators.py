from django.core.exceptions import ValidationError
from datetime import date
import re
import os
import logging

logger = logging.getLogger(__name__)


def real_age(value: date) -> None:
    age = (date.today() - value).days / 365
    if age < 1 or age > 80:
        raise ValidationError(
            'Возраст от 1 года до 80 лет'
        )


def real_number(value) -> None:
    regex = r'^\+?[78]{1}[\s\(]{,2}\d{3}[\s\)]{,2}\d{3}[\s-]?\d{2}[\s-]?\d{2}'
    match = re.match(regex, value)
    if match is None:
        raise ValidationError(
            'Номер телефона не подходит'
        )


def real_email(value) -> None:
    regex = r'^[a-zA-Z0-9\-\_]+\@(gmail\.com|mail\.ru|edu\.ru)'
    match = re.match(regex, value)
    if match is None:
        raise ValidationError(
            'Почта не подходит'
        )
    

def validate_image_file(value):
    """Валидатор для проверки, что файл является изображением"""
    ext = os.path.splitext(value.name)[1].lower()
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    
    if ext not in valid_extensions:
        logger.warning(f"Invalid file type uploaded: {ext}")
        raise ValidationError(f'Неверный формат файла. Поддерживаются: {", ".join(valid_extensions)}')
