from django.core.exceptions import ValidationError
from django.db import models
from django.utils.timezone import now


class Course(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name='Назва')
    start_date = models.DateField(
        blank=False, verbose_name='Дата початку',
        default=now
        )
    end_date = models.DateField(
        blank=False, verbose_name='Дата закінчення'
        )
    lectures_amount = models.PositiveIntegerField(
        blank=False,
        verbose_name='Кількість лекцій'
        )

    def __str__(self):
        return self.name

    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError(
                'Дата закінчення не можке бути раніше дати '
                'початку'
                )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курси"
