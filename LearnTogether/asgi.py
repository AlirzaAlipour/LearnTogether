import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from communications import routing as communications_routing 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learntogether.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            communications_routing.websocket_urlpatterns 
        )
    ),
})