from django.urls import path, include
from watchlist_app.api.views import StreamPlatformAV, StreamPlatformDetailsAV, WatchListAV, WatchListDetailsAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>/', WatchListDetailsAV.as_view(), name='watch-list-details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>/', StreamPlatformDetailsAV.as_view(), name='stream-details'),
]
