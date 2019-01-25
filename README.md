[![Build Status](https://travis-ci.org/nickdelgrosso/mini_proteindb.svg?branch=master)](https://travis-ci.org/nickdelgrosso/mini_proteindb)
[![Coverage Status](https://coveralls.io/repos/github/nickdelgrosso/mini_proteindb/badge.svg?branch=master)](https://coveralls.io/github/nickdelgrosso/mini_proteindb?branch=master)

# ProteinDB

A small demo of how to use sqlite in python and BioPy to read fasta files and put them in databases.  

Provides a ProteinDB class that can be populated with fasta files and queried by uniprot id and sequence.

## Installation
```
pip install proteindb
```

## Usage

```python
from proteindb import ProteinDB
>> db = ProteinDB('human_proteome.db')  # Creates an sqlite database with that filename.

>> db.populate('uniprot1.fasta')

>> db.query(uniprot_id='DFAFDA1')
>> db.result
'SDFYUONNAJDMAMDFHAABWQ'

>> db.query(sequence='SDFYUONNAJDMAMDFHAABWQ')
>> db.result
'DFAFDA1'
```  
