from Bio import Entrez
Entrez.email = "localuser@localhost.localdomain"
handle = Entrez.esearch(db="nuccore", term="Occidozyga")
record = Entrez.read(handle)
print(record["IdList"])