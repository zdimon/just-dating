from channels.routing import ProtocolTypeRouter, URLRouter
from online.online_consumer import OnlineConsumer
from django.urls import re_path
from channels.auth import AuthMiddlewareStack


websocket_urlpatterns = [
    re_path(r'online/$', OnlineConsumer),
]

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ), 
})
