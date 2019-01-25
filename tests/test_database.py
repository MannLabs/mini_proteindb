from proteindb import ProteinDB
import sqlite3
import pytest

@pytest.fixture
def db():
    return ProteinDB('test.db')

@pytest.fixture
def cursor(db):
    conn = db._conn
    return conn.cursor()

def test_proteindb_contains_database(db):
    assert isinstance(db._conn, sqlite3.Connection)


def test_db_contains_protein_table(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    results = cursor.fetchall()
    assert len(results) == 1
    assert results[0][0] == 'proteins'

def test_db_table_contains_all_columns(cursor):
    cursor.execute("PRAGMA table_info('proteins');")
    results = cursor.fetchall()
    columns = [result[1] for result in results]
    assert 'uniprot_id' in columns and 'sequence' in columns
