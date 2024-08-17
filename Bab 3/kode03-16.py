from Bio import Entrez
Entrez.email = "localuser@localhost.localdomain" 
handle = Entrez.egquery(term="Limnonectes")
record = Entrez.read(handle)
print(record.keys())
