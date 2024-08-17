from Bio import Entrez
Entrez.email = "localuser@localhost.localdomain" 
efetch_handle = Entrez.efetch(db = "nuccore", id = "OM037657", rettype = "fasta", retmode = "text")
fasta_record = efetch_handle.read()
print(fasta_record)