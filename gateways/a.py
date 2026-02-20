import socket
from gateways.gateway import listen_to_socket

if __name__ == "__main__":
    listen_to_socket(9000, 10)
