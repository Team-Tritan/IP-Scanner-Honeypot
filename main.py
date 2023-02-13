import socket
import logging
import threading
import time

logging.basicConfig(filename="requests.log", level=logging.INFO)


def create_listeners(first, last):
    try:
        for i in range(first, last):
            t = threading.Thread(target=handle_threads, args=(i,))
            t.start()
    except Exception as e:
        print("Error creating thread for {}".format(i), e)
        return


def handle_threads(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("", port))
        s.listen(1)
        print("Listening on port {}".format(port))
    except Exception as e:
        print("Error binding to port {}".format(port), e)
        return
    try:
        while True:
            conn, addr = s.accept()
            with conn:
                current_time = time.localtime()
                logging.info("{}".format(current_time))
                logging.info("Connected by {}".format(addr))
                print("{} - Connected by {}".format(current_time, addr))
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    logging.info("{}".format(current_time))
                    logging.info("Received data: {}".format(data.decode()))
                    print("Received data: {}".format(data.decode()))
                    conn.send(b"fuck you chinese heckers!")

    except Exception as e:
        print("Error in thread {}".format(port), e)
        return


if __name__ == "__main__":
    create_listeners(80, 65535)
