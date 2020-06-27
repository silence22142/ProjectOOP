import socket
sock = socket.socket()


class Data:
    def __init__(self):
        self.selected = ""
        self.games = {}
        self.rates = {}
        self._get_game_data()

    def _get_game_data(self):
        file = open('rates.txt', 'r')
        send_data = file.readline()
        sock.connect(("localhost", 9090))
        sock.send(send_data.encode())
        data = sock.recv(4096).decode()
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        items = data.split(":")
        for item in items:
            game = item.split("/")
            self.games[game[0]] = game[1:]

    def get_value(self):
        return self.games[self.selected]

    def send_rate(self, rate):
        data = self.get_value()
        self.rates[data[0]] = str(rate)

    def save_rates(self):
        file = open('rates.txt', 'w')
        data = []
        for game in self.rates:
            data.append(self.rates[game] + ":" + game)
        record = "/".join(data)
        if record:
            file.write(record)
        else:
            file.write("1")
        file.close()
