from channels.routing import route
from mainApp.consumers import *

channel_routing = [
        # route('http.request', 'mainApp.consumers.http_consumer'),
        route('websocket.connect', ws_add, path=r"^/user1/$",),
        route('websocket.receive', ws_message, path=r"^/user1/$",),
        route('websocket.connect', ws_add2, path=r"^/user2/$",),
        route('websocket.receive', ws_message2, path=r"^/user2/$",),
        route('websocket.disconnect', ws_disconnect),
        ]
