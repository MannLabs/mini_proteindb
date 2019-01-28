import pytest
from pytest_bdd import scenario, given, when, then, scenarios
from proteindb import ProteinDB
from os import path


@pytest.fixture
def Workspace():
    """A singleton object representing the variables in memory in a session."""
    class Workspace:
        pass
    return Workspace

@given("I have a database populated with data from Fasta file named <filename>.")
def db(filename):
    db = ProteinDB()
    db.populate(path.join('data', filename))
    return db


#####
@scenario('protein_database.feature', "Sequence Search by ID")
def test_search_by_ID():
    pass


@given("<uniprot_id>")
def uniprot_id(uniprot_id):
    return uniprot_id


@when("I search for <uniprot_id> in a database")
def step_impl(db, uniprot_id, Workspace):
    Workspace.result = db.query(uniprot_id=uniprot_id)


@then("I will see the corresponding <sequence>")
def step_impl(Workspace, sequence):
    assert Workspace.result == sequence


#############
@scenario('protein_database.feature', "ID Search by Sequence")
def test_search_by_ID():
    pass

@given("<sequence>")
def sequence(sequence):
    return sequence



@when("I search for the <sequence> in the database")
def step_impl(db, sequence, Workspace):
    Workspace.result = db.query(sequence=sequence)


@then("I will see the corresponding <uniprot_id>")
def step_impl(uniprot_id, Workspace):
    assert Workspace.result == uniprot_id

