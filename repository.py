import json


class Repository():
    def __init__(self):
        self.file_path = None

    def set_file_path(self, file_path):
        self.file_path = file_path

        return self

    def load(self):
        with open(self.file_path, "r") as f:
            return json.load(f)

        return []