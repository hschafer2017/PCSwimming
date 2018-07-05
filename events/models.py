from __future__ import unicode_literals
from django.db import models


# Create your models here - EVENTS.

class Event(models.Model):
    name = models.CharField(max_length=200)
    day = models.DateField(u'Day of event', help_text=u'Day of the event')
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    end_time = models.TimeField(u'Final time', help_text=u'Final Time')
    location = models.CharField(max_length=200)
    notes = models.TextField(u'Textual Notes', help_text=u'Textaul Notes', blank = True, null = True)
    
    def __str__(self):
        return self.name
