from Bio import Entrez
Entrez.email = "localuser@localhost.localdomain" 
handle = Entrez.efetch(db="nuccore", id="ON860685", rettype="gb",retmode="text")
print(handle.read())