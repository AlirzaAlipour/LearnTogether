from django.urls import re_path
from .consumers import ChatConsumer 



websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<username>[\w.@+-]+)/$', ChatConsumer.as_asgi()),  # When using re_path, the pattern is treated as a regular expression.
]

