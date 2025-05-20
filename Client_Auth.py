import socket
import zlib
import numpy as np
import cv2
import getpass  # For hidden password input

WINDOW_NAME = "Remote Screen"

def send_authentication(s, username, password):
    s.send(len(username).to_bytes(1, 'big') + username.encode())
    s.send(len(password).to_bytes(1, 'big') + password.encode())

def receive_frames(server_ip, port):
    print(f"[INFO] Connecting to {server_ip}:{port}...")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((server_ip, port))
        print("[INFO] Connected.")

        # Get username and password from user
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")

        send_authentication(s, username, password)

        response = s.recv(2)
        if response != b'OK':
            print("[ERROR] Authentication failed. Closing connection.")
            s.close()
            return
        print("[INFO] Authentication successful. Receiving frames...")

        while True:
            data = s.recv(4)
            if not data:
                print("[INFO] Server disconnected.")
                break

            frame_len = int.from_bytes(data, 'big')
            buffer = b''

            while len(buffer) < frame_len:
                packet = s.recv(frame_len - len(buffer))
                if not packet:
                    print("[ERROR] Connection closed unexpectedly.")
                    return
                buffer += packet

            try:
                decoded = zlib.decompress(buffer)
                nparr = np.frombuffer(decoded, np.uint8)
                frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

                if frame is not None:
                    cv2.imshow(WINDOW_NAME, frame)
                    if cv2.waitKey(1) == ord('q'):
                        print("[INFO] Exit requested by user.")
                        break
                else:
                    print("[WARNING] Received an empty frame.")
            except Exception as e:
                print(f"[ERROR] Decoding failed: {e}")
                continue

    except ConnectionRefusedError:
        print(f"[ERROR] Cannot connect to {server_ip}:{port}. Is the server running?")
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        print("[INFO] Closing connection and cleaning up.")
        s.close()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Prompt user for server IP and port
    SERVER_IP = input("Enter server IP address: ").strip()
    while True:
        port_input = input("Enter server port (default 8888): ").strip()
        if port_input == '':
            PORT = 8888
            break
        elif port_input.isdigit() and 0 < int(port_input) < 65536:
            PORT = int(port_input)
            break
        else:
            print("Invalid port. Please enter a number between 1 and 65535.")

    receive_frames(SERVER_IP, PORT)
