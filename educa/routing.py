import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing  # your app-level websocket routes

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educa.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # normal HTTP requests
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns  # use app-level routes
        )
    ),
})
