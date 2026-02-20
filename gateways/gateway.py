import socket


def listen_to_socket(port: int, n_accepts: int):
    sock = socket.socket()
    sock.bind(("127.0.0.1", port))
    sock.listen()

    while True:
        conn, _ = sock.accept()
        if n_accepts > 0:
            _ = conn.send(b"000")
            print(f"accepted by gateway at port {port}")

        conn.close()
