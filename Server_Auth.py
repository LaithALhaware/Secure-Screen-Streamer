import socket
import threading
import mss
import zlib
import cv2
import numpy as np

HOST = '0.0.0.0'
PORT = 8888

# Simple user database
users = {
    "admin": "pass123",
    "laith": "secure456"
}

def send_frames(conn):
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Full screen
        while True:
            img = sct.grab(monitor)
            frame = np.array(img)
            _, encoded = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 50])
            compressed = zlib.compress(encoded.tobytes())

            try:
                conn.sendall(len(compressed).to_bytes(4, 'big') + compressed)
            except:
                break

def authenticate(conn):
    try:
        # Receive username length and username
        user_len = int.from_bytes(conn.recv(1), 'big')
        username = conn.recv(user_len).decode()

        # Receive password length and password
        pass_len = int.from_bytes(conn.recv(1), 'big')
        password = conn.recv(pass_len).decode()

        print(f"[INFO] Authentication attempt: {username}")

        if users.get(username) == password:
            conn.send(b'OK')  # Send success signal
            return True
        else:
            conn.send(b'NO')  # Send failure signal
            return False

    except Exception as e:
        print(f"[ERROR] Authentication error: {e}")
        return False

def handle_client(conn, addr):
    if authenticate(conn):
        print(f"[INFO] {addr} authenticated successfully.")
        send_frames(conn)
    else:
        print(f"[WARNING] {addr} failed authentication.")
        conn.close()

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    print(f"[+] Listening on {HOST}:{PORT}")

    while True:
        conn, addr = s.accept()
        print(f"[+] Client connected: {addr}")
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    start_server()
