from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.text

    def is_recent(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date <  now
        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'

class Option(models.Model):
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.text

