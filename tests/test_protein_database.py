from pytest_bdd import scenario, given, when, then

@scenario('protein_database.feature', 'Populating the Database')
def test_pytest_runs():
    assert True