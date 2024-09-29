from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.list_events, name='list_events'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('proxy/events/<int:event_id>/', views.proxy_event_detail, name='proxy_event_detail'),
    path('tag/<str:tag_name>/', views.FilterEventsByTagView, name='filter_events'),
    path('proxy/events/filter/', views.proxy_filter_events_by_tag, name='proxy_filter_events_by_tag'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
