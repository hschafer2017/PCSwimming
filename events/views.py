from django.shortcuts import render
from .models import Event, Document

"""All visitors to the site have access to the events page. Upcoming swim
meet information can be found in this app."""


def get_events(request):
    events = Event.objects.all()
    documents = Document.objects.all()
    return render(request, 'events/events.html', {'events': events,
                  'documents': documents})
