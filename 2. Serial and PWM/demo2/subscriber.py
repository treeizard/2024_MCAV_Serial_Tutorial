import cv2
import numpy as np
import socket
import struct

def receive_image_via_wifi(host, port):
    # Create a socket and bind it to the host and port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(0)  # Listen for incoming connections
    print(f"Waiting for connection on {host}:{port}...")

    try:
        while True:
            # Accept a single connection
            client_socket, addr = server_socket.accept()
            print(f"Connected to {addr}")

            # Receive and display images continuously
            while True:
                try:
                    # Receive image size
                    img_size_bytes = client_socket.recv(4)
                    if len(img_size_bytes) == 0:
                        break
                    img_size = struct.unpack(">L", img_size_bytes)[0]

                    # Receive image data
                    img_bytes = b""
                    while len(img_bytes) < img_size:
                        packet = client_socket.recv(img_size - len(img_bytes))
                        if not packet:
                            break
                        img_bytes += packet

                    # Decode image bytes
                    nparr = np.frombuffer(img_bytes, np.uint8)
                    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

                    # Display the received image
                    cv2.imshow("Received Image", frame)

                    # Break the loop if 'q' is pressed
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        raise KeyboardInterrupt
                except KeyboardInterrupt:
                    break

            # Clean up for the current connection
            client_socket.close()

    except KeyboardInterrupt:
        print("Exiting...")
        # Clean up
        server_socket.close()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    host = '0.0.0.0'  # Bind to all available interfaces
    port = 9999  # Port number to listen on
    receive_image_via_wifi(host, port)