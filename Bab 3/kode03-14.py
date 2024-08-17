from Bio import Entrez
Entrez.email = "localuser@localhost.localdomain" 
handle = Entrez.esummary(db = "nuccore", id = "KU950323")
print(handle.read())