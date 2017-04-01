from channels.routing import route
from mainApp.consumers import *

channel_routing = [
        # route('http.request', 'mainApp.consumers.http_consumer'),
        route('websocket.connect', ws_add),
        route('websocket.disconnect', ws_disconnect),
        route('websocket.receive', ws_message),
        ]
