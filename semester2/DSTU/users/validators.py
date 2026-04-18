from django.core.exceptions import ValidationError
from datetime import date
import re


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
