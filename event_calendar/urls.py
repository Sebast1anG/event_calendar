from django.contrib import admin
from django.urls import path, include
from events import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.calendar_view, name='home'),
    path('events/', include('events.urls')),
    path('proxy/events/', views.proxy_events, name='proxy_events'),
    path('proxy/events/filter/', views.proxy_filter_events_by_tag, name='proxy_filter_events_by_tag'),
    path('proxy/events/<int:event_id>/', views.proxy_event_detail, name='proxy_event_detail'),
]