import sqlite3
from Bio import SeqIO

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

    def populate(self, fasta_filename):
        cursor = self._conn.cursor()
        with open(fasta_filename) as f:
            for idx, record in enumerate(SeqIO.parse(f, 'fasta')):
                uniprot_id = record.id.split('|')[1]
                sequence = str(record.seq)
                sql = "INSERT INTO proteins(id, uniprot_id, sequence) VALUES(?,?,?)"
                cursor.execute(sql, (idx, uniprot_id, sequence))


    def query(self, uniprot_id=None, sequence=None):
        self._conn.query(query_string)
        self.result = self._conn.get_result()
