from django.core.validators import RegexValidator
from django.db import models


ACCESS_LEVEL_CHOICES = [
    ('green', 'Green'),
    ('blue', 'Blue'),
    ('purple', 'Purple'),
]


class Card(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=8,
        unique=True,
        validators=[RegexValidator(r'^[0-9A-F]{8}$', 'ID must be 8 hexadecimal characters')],
    )
    access_level = models.CharField(max_length=20, choices=ACCESS_LEVEL_CHOICES, default='green')

    def __str__(self):
        return f'Card {self.id} - {self.access_level}'
