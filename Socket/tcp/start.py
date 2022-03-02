import TCP_server
import TCP_client
from threading import Thread


server_thread = Thread(target=TCP_server.main)
client_thread = Thread(target=TCP_client.main)


server_thread.start()
client_thread.start()
