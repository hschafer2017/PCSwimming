from __future__ import unicode_literals
 
from django.contrib import admin
from .models import Event, Document


admin.site.register(Event)
admin.site.register(Document)
