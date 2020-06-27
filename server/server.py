import socket
from Controller import controller
sock = socket.socket()
sock.bind(('localhost', 9090))
sock.listen(10)
control = controller.Controller()

while True:
    try:
        conn, addr = sock.accept()
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        data_raw = conn.recv(1024)
        decoded_data = data_raw.decode()
        if decoded_data == "No data":
            conn.send(control.get_all_games().encode())
            conn.close()
            continue
        for item in decoded_data.split("/"):
            parts = item.split(":")
            control.update_user_rate(int(parts[0]), int(parts[1]))
        conn.send(control.get_all_games().encode())
        conn.close()
