import cv2
import numpy as np
import socket
import pickle
import struct
import depthai as dai



def stream_image_via_wifi(image, host, port):
    # Connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
    except socket.error as e:
        print(f"Error: Couldn't connect to the server: {e}")
        return

    # Serialize and send image
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    _, img_encoded = cv2.imencode('.jpg', image, encode_param)
    img_bytes = img_encoded.tobytes()
    img_size = len(img_bytes)
    try:
        client_socket.sendall(struct.pack(">L", img_size) + img_bytes)
    except socket.error as e:
        print(f"Error: Couldn't send image data: {e}")
        client_socket.close()
        return

    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    #Set up the stream
    pipeline = dai.Pipeline()

    camRgb = pipeline.create(dai.node.ColorCamera)
    xoutRgb = pipeline.create(dai.node.XLinkOut)

    xoutRgb.setStreamName("rgb")

    # Properties
    camRgb.setPreviewSize(300, 300)
    camRgb.setInterleaved(False)
    camRgb.setColorOrder(dai.ColorCameraProperties.ColorOrder.RGB)

    # Linking
    camRgb.preview.link(xoutRgb.input)
    
    # Basic
    host = '192.168.68.61'  # IP address of the receiving device
    port = 9999  # Port number to listen on the receiving device
    with dai.Device(pipeline) as device:
        qRgb = device.getOutputQueue(name="rgb", maxSize=4, blocking=False)
        

        while True:
            # Capture an image
            #image = capture_image()
            inRgb = qRgb.get()  # blocking call, will wait until a new data has arrived
            frame =  inRgb.getCvFrame()
            # Retrieve 'bgr' (opencv format) frame
            cv2.imshow("rgb",frame)
            #print(type(frame))
            stream_image_via_wifi(frame, host, port)
            if cv2.waitKey(1) == ord('q'):
                break
            