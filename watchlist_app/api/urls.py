from watchlist_app.models import Review
from django.urls import path
from watchlist_app.api.views import ReviewDetail, ReviewList, ReviewCreate, StreamPlatformAV, StreamPlatformDetailsAV, WatchListAV, WatchListDetailsAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>/', WatchListDetailsAV.as_view(), name='watch-list-details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>/', StreamPlatformDetailsAV.as_view(), name='streamplatform-detail'),
    path('<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-details'),
]
