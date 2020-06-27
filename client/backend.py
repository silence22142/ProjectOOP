import socket
sock = socket.socket()
sock.connect(("localhost", 9090))


class Data:
    def __init__(self):
        self.selected = ""
        self.games = {}
        self.rates = {}
        self._get_game_data()

    def _get_game_data(self):
        data = sock.recv(4096).decode()
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
        data = []
        for game in self.rates:
            data.append(self.rates[game] + ":" + game)
        record = "/".join(data)
        if record:
            sock.send(record.encode())
            sock.close()
        else:
            sock.send("No data".encode())
            sock.close()
