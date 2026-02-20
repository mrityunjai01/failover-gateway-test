import socket

SUCCESS_MSG = r"""HTTP/1.1 400 Bad Request
Content-Type: application/json
Content-Length: 71

{
  "error": "Bad request",
  "message": "Request body could not be read properly.",
}
"""

FAIL_MSG = r"""HTTP/1.1 200 OK
Content-Type: application/text
a
"""


def listen_to_socket(port: int, n_accepts: int):
    sock = socket.socket()
    sock.bind(("127.0.0.1", port))
    sock.listen()

    while True:
        conn, _ = sock.accept()
        conn.recv(1024)
        if n_accepts > 0:
            _ = conn.sendall(b"HTTP/1.0 200 OK\r\n")
            print(f"accepted by gateway at port {port}")
            n_accepts -= 1
        else:
            _ = conn.sendall(b"HTTP/1.0 400 Bad Request\r\n")
            print(f"rejected by gateway at port {port}")

        conn.close()
