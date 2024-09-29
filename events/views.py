from django.shortcuts import render
from django.http import JsonResponse
from .service import EventAPIService
import requests

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
    api_url = 'https://rekrutacja.teamwsuws.pl/events/'
    headers = {
        'api-key': 'b35768c1ac5cca77dea0f657095f03de',
    }
    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            return JsonResponse(response.json(), safe=False)
        else:
            return JsonResponse({'error': 'Błąd API'}, status=response.status_code)
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

def proxy_event_detail(request, event_id):
    api_url = f'https://rekrutacja.teamwsuws.pl/events/{event_id}/'
    headers = {
        'api-key': 'b35768c1ac5cca77dea0f657095f03de',
    }
    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            return JsonResponse(response.json(), safe=False)
        else:
            return JsonResponse({'error': 'Błąd API'}, status=response.status_code)
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
        

def proxy_filter_events_by_tag(request):
    tag = request.GET.get('tag')
    if not tag:
        return JsonResponse({'error': 'Tag parameter is missing'}, status=400)
    
    api_url = f'https://rekrutacja.teamwsuws.pl/events/filter/?tag={tag}'
    headers = {
        'api-key': 'b35768c1ac5cca77dea0f657095f03de',
    }
    
    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            return JsonResponse(response.json(), safe=False)
        else:
            return JsonResponse({'error': 'Błąd API'}, status=response.status_code)
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
