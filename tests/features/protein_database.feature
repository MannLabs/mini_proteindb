Feature: Protein Database

  Scenario Outline: Populating the Database
    Given I have a Fasta file named <filename> that contains protein sequences
    When I populate a protein database with the Fasta files
    Then all the sequences from the Fasta files are inside the database

    Examples: Vertical
    | filename | uni6283.fasta |

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

