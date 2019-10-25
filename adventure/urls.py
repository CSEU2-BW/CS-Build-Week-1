from django.conf.urls import url
from . import api

urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
    # add the api to fetch alll rooms
    url('fetch_rooms', api.fetchRoom),
]