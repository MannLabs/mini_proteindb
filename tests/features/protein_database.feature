@todo
Feature: Protein Database

  Examples: Vertical
    | filename   | uni6283.fasta |
    | uniprot_id | dsafnadf1     |
    | sequence   | ADNFADFHJ     |

  Background:
    Given I have a database populated with data from Fasta file named <filename>.

  Scenario: Sequence Search by ID
    Given <uniprot_id>
    When I search for <uniprot_id> in a database
    Then I will see the corresponding <sequence>

  Scenario: ID Search by Sequence
    Given <sequence>
    When I search for the <sequence> in the database
    Then I will see the corresponding <uniprot_id>

