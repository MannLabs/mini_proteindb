Feature: Protein Database

  Background: Creating the Database
    Given I have a database filename
    When I build the database
    Then I should see a protein database file

  Scenario: Populating the Database
    Given I have some Fasta files that contain protein sequences
    When I populate a protein database with the Fasta files
    Then all the sequences from the Fasta files are inside the database

  Scenario: Sequence Search by ID
    Given the protein database
    And and a Uniprot ID
    When I search for ID in a database
    Then I will see the sequence associated with the ID

  Scenario: ID Search by Sequence
    Given a sequence
    And and the protein database
    When I search for the sequence in the database
    Then I will see all IDs associated with the sequence

