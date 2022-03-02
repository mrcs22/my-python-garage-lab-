import os
import UDP_server
import UDP_client
from threading import Thread


server_thread = Thread(target=UDP_server.main)
client_thread = Thread(target=UDP_client.main)


server_thread.start()
client_thread.start()
