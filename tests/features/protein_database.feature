Feature: Protein Database

  Scenario: Populating the Database
    Given I have some Fasta files
    And the Fasta files contain protein sequences
    When I build a protein database
    Then I should see a protein database file
    And all the sequences from the Fasta files are inside the database

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

