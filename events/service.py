import requests
from django.conf import settings

class EventAPIService:
    BASE_URL = 'https://rekrutacja.teamwsuws.pl/events/'

    @classmethod
    def get_headers(cls):
        return {'api-key': settings.EVENT_API_KEY}

    @classmethod
    def get_events(cls):
        headers = cls.get_headers()
        response = requests.get(cls.BASE_URL, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return []

    @classmethod
    def get_event_details(cls, event_id):
        headers = cls.get_headers()
        response = requests.get(f"{cls.BASE_URL}{event_id}/", headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    @classmethod
    def filter_events_by_tag(cls, tag):
        headers = cls.get_headers()
        response = requests.get(f"{cls.BASE_URL}filter/?tag={tag}", headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return []
