from proteindb import ProteinDB
import sqlite3

def test_proteindb_contains_database():
    db = ProteinDB('test.db')
    assert isinstance(db.db, sqlite3.Connection)