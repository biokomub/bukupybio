from Bio import Entrez
Entrez.email = "localuser@localhost.localdomain" 
pmid = {
    "journal_title": "Zoolog Sci",
    "year": "2010", 
    "volume": "27", 
    "first_page": "222",
    "author_name": "kurniawan n", 
    "key": "pmid"}
record = Entrez.ecitmatch(db="pubmed", rettype="xml", bdata=[pmid])
print(record.read())