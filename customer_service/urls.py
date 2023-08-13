from django.urls import path
from .views import *

urlpatterns = [
    path('submit_request/', submit_request, name='submit_request'),
    path('track_request/<int:request_id>', track_request, name='track_request'),
    path('support/', support_dashboard, name='support_dashboard'),
    path('home/', dashboard, name='dashboard'),
]