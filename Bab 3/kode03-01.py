from Bio import Entrez
Entrez.email = "localuser@localhost.localdomain" 
handle = Entrez.einfo()
print(handle.read())