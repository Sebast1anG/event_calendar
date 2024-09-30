from django.shortcuts import render
from django.http import JsonResponse
from .service import EventAPIService

def ListEventsView(request):
    events = EventAPIService.get_events()
    return JsonResponse(events, safe=False)

def event_detail(request, event_id):
    event = EventAPIService.get_event_details(event_id)
    if event:
        return JsonResponse(event, safe=False)
    else:
        return JsonResponse({'error': 'Event not found'}, status=404)

def FilterEventsByTagView(request, tag_name):
    filtered_events = EventAPIService.filter_events_by_tag(tag_name)
    return JsonResponse(filtered_events, safe=False)

def calendar_view(request):
    return render(request, 'calendar.html')

def list_events(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})

def proxy_events(request):
    events = EventAPIService.get_events()
    return JsonResponse(events, safe=False)

def proxy_event_detail(request, event_id):
    event = EventAPIService.get_event_details(event_id)
    if event:
        return JsonResponse(event, safe=False)
    else:
        return JsonResponse({'error': 'Błąd API'}, status=404)

def proxy_filter_events_by_tag(request):
    tag = request.GET.get('tag')
    if not tag:
        return JsonResponse({'error': 'Tag parameter is missing'}, status=400)
    
    filtered_events = EventAPIService.filter_events_by_tag(tag)
    return JsonResponse(filtered_events, safe=False)
