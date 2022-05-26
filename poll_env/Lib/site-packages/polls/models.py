import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


class Question(models.Model):
    """The question for the poll."""

    text = models.CharField(max_length=200)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """A string representation of the model."""
        return self.text

    def was_published_recently(self):
        """Checks whether the question was published recently.
        How recent? last 24 hours."""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.published_date <= now


class Choice(models.Model):
    """The options for the question."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """A string representation of the model."""
        return self.text
