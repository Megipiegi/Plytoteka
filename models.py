import json

class Plytoteka:
    def __init__(self):
        try:
            with open("plytoteka.json", "r") as f:
                self.plytoteka = json.load(f)
        except FileNotFoundError:
            self.plytoteka = []

    def all(self):
        return self.plytoteka

    def get(self, id):
        return self.plytoteka[id]

    def create(self, data):
        data.pop('csrf_token')
        self.plytoteka.append(data)

    def save_all(self):
        with open("plytoteka.json", "w") as f:
            json.dump(self.plytoteka, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.plytoteka[id] = data
        self.save_all()

    def delete(self, id):
        abc = self.get(id)
        self.plytoteka.remove(abc)
        self.save_all()


plytoteka = Plytoteka()