from django.shortcuts import render
from .models import Event, Document

# Create your views here.

def get_events(request):
    events = Event.objects.all()
    documents = Document.objects.all()
    return render(request, 'events/events.html', {'events': events, 'documents': documents})
