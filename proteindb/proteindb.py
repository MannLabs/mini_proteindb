
class ProteinDB:
    def __init__(self):
        self.db = None
        self.result = None

    def populate(self, filename):
        pass

    def query(self, query_string):
        self.db.query(query_string)
        self.result = self.db.get_result()