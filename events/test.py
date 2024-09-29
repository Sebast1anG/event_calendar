from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch

class EventsTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
    
    @patch('events.views.requests.get')
    def test_proxy_events_success(self, mock_get):
        mock_response = {
            "events": [
                {
                    "id": 1,
                    "name": "Test Event",
                    "start_time": "2024-09-01T10:00:00",
                    "short_description": "This is a test event."
                }
            ]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        
        response = self.client.get(reverse('proxy_events'))
        self.assertEqual(response.status_code, 200)
        self.assertIn("Test Event", response.content.decode())
    
    @patch('events.views.requests.get')
    def test_proxy_event_detail_success(self, mock_get):
        mock_response = {
            "id": 1,
            "name": "Test Event",
            "start_time": "2024-09-01T10:00:00",
            "short_description": "This is a test event."
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        
        response = self.client.get(reverse('proxy_event_detail', kwargs={'event_id': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertIn("Test Event", response.content.decode())

    @patch('events.views.requests.get')
    def test_proxy_filter_events_by_tag_success(self, mock_get):
        mock_response = {
            "events": [
                {
                    "id": 1,
                    "name": "uws event",
                    "start_time": "2024-09-01T10:00:00",
                    "tags": [{"name": "uws"}]
                }
            ]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        
        response = self.client.get(reverse('proxy_filter_events_by_tag') + '?tag=uws')
        self.assertEqual(response.status_code, 200)
        self.assertIn("uws event", response.content.decode())


