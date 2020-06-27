import socket
from Controller import controller
import threading
sock = socket.socket()
sock.bind(('localhost', 9090))
sock.listen(10)
control = controller.Controller()


def process_new_client(clientsock):
    clientsock.send(control.get_all_games().encode())
    data_raw = conn.recv(1024)
    decoded_data = data_raw.decode()
    if decoded_data == "No data":
        conn.close()
        print("Connection close")
        return
    for item in decoded_data.split("/"):
        parts = item.split(":")
        control.update_user_rate(int(parts[0]), int(parts[1]))
    conn.close()
    print("Connection close")


while True:
    try:
        conn, addr = sock.accept()
        print("Connection from", addr)
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        new_thread = threading.Thread(target=process_new_client, args=(conn, ))
        new_thread.start()
