from Bio import Entrez
Entrez.email = "localuser@localhost.localdomain" 
handle_efetch = Entrez.efetch(db="nuccore", id="1917890951", rettype="gb", retmode="text")
info = handle_efetch.read()
print(info)