"""Stage 3: Socket verification for X-ray file transfer and clinical chat."""
import socket
import threading
import time

def server(port_holder, ready_event):
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind(("127.0.0.1", 0))
    srv.listen(2)
    port_holder.append(srv.getsockname()[1])
    ready_event.set()

    # 1. Receive chat message
    chat_conn, _ = srv.accept()
    with chat_conn:
        msg = chat_conn.recv(1024).decode()
        chat_conn.sendall(b"DELIVERED: " + msg.encode())

    # 2. Receive 500 KB X-ray payload
    file_conn, _ = srv.accept()
    received = 0
    with file_conn:
        while True:
            chunk = file_conn.recv(4096)
            if not chunk:
                break
            received += len(chunk)
    srv.close()
    print(f"Server verified {received} bytes of X-ray data.")

if __name__ == "__main__":
    port_holder = []
    ready_event = threading.Event()
    th = threading.Thread(target=server, args=(port_holder, ready_event))
    th.start()
    ready_event.wait()
    port = port_holder[0]

    # Chat client
    c1 = socket.create_connection(("127.0.0.1", port))
    t0 = time.time()
    c1.sendall(b"Patient vitals stable.")
    reply = c1.recv(1024).decode()
    print("Chat:", reply, f"in {(time.time() - t0) * 1000:.2f} ms")
    c1.close()

    # File client (500 KB X-ray)
    c2 = socket.create_connection(("127.0.0.1", port))
    t1 = time.time()
    c2.sendall(b"X" * 500_000)
    c2.close()
    th.join()
    print(f"500 KB X-ray transfer completed in {(time.time() - t1) * 1000:.2f} ms")
