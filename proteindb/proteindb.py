import sqlite3


class ProteinDB:
    def __init__(self, filename='protein.db'):
        self.db = sqlite3.connect(filename)
        self.result = None

    def populate(self, filename):
        pass

    def query(self, query_string):
        self.db.query(query_string)
        self.result = self.db.get_result()