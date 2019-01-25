from proteindb import ProteinDB
import sqlite3

def test_proteindb_contains_database():
    db = ProteinDB('test.db')
    assert isinstance(db._conn, sqlite3.Connection)


def test_db_contains_protein_table():
    db = ProteinDB('test.db')
    conn = db._conn
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    results = c.fetchall()
    assert len(results) == 1
    assert results[0][0] == 'proteins'

def test_db_table_contains_all_columns():
    db = ProteinDB('test.db')
    conn = db._conn
    c = conn.cursor()
    c.execute("PRAGMA table_info('proteins');")
    results = c.fetchall()
    columns = [result[1] for result in results]
    assert 'uniprot_id' in columns and 'sequence' in columns
