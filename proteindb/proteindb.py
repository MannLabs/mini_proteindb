import sqlite3


def setup_db(filename):
    conn = sqlite3.connect(filename)
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE proteins
                             (id INTEGER, uniprot_id TEXT, sequence TEXT)''')
        c.execute("PRAGMA table_info('proteins');")
    except sqlite3.OperationalError as e:
        if 'already exists' in str(e):
            pass
        else:
            raise e
    conn.commit()
    return conn


class ProteinDB:
    def __init__(self, filename='protein.db'):
        self._conn = setup_db(filename)
        self.result = None

    def populate(self, filename):
        pass

    def query(self, query_string):
        self._conn.query(query_string)
        self.result = self._conn.get_result()
