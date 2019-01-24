from pytest_bdd import scenario, given, when, then

@scenario("protein_database.feature", "Creating the Database")
def test_db():
    pass

@given("I have a database filename")
def file_name():
    raise NotImplemented

@when("I build the database")
def build_database(file_name):
    return database

@then("I should see a protein database file")
def check_database(database):
    raise NotImplemented

@scenario('protein_database.feature', 'Populating the Database')
def test_foo():
    pass

@given("I have some Fasta files that contain protein sequences")
def fasta():
    raise NotImplemented

@when("I populate a protein database with the Fasta files")
def build_and_populate_database(fasta):
    raise NotImplemented

@then("all the sequences from the Fasta files are inside the database")
def database_contains_all_sequences(database, fasta):
    raise NotImplemented

@scenario('protein_database.feature', "Sequence Search by ID")
def test_search_by_ID():
    pass

@given("the protein database")
def step_impl():
    raise NotImplementedError(u'STEP: Given the protein database')


@given("and a Uniprot ID")
def step_impl():
    raise NotImplementedError(u'STEP: And and a Uniprot ID')


@when("I search for ID in a database")
def step_impl():
    raise NotImplementedError(u'STEP: When I search for ID in a database')


@then("I will see the sequence associated with the ID")
def step_impl():
    raise NotImplementedError(u'STEP: Then I will see the sequence associated with the ID')

@scenario('protein_database.feature', "ID Search by Sequence")
def test_search_by_ID():
    pass

@given("a sequence")
def step_impl():
    raise NotImplementedError(u'STEP: Given a sequence')


@given("and the protein database")
def step_impl():
    raise NotImplementedError(u'STEP: And and the protein database')


@when("I search for the sequence in the database")
def step_impl():
    raise NotImplementedError(u'STEP: When I search for the sequence in the database')


@then("I will see all IDs associated with the sequence")
def step_impl():
    raise NotImplementedError(u'STEP: Then I will see all IDs associated with the sequence')