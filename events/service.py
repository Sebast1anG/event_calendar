import requests

class EventAPIService:
    BASE_URL = 'https://rekrutacja.teamwsuws.pl/events/'
    API_KEY = 'b35768c1ac5cca77dea0f657095f03de'

    @classmethod
    def get_events(cls):
        headers = {'api_key': cls.API_KEY}
        response = requests.get(cls.BASE_URL, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return []

    @classmethod
    def get_event_details(cls, event_id):
        headers = {'api_key': cls.API_KEY}
        response = requests.get(f"{cls.BASE_URL}{event_id}/", headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return None
