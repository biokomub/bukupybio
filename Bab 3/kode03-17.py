from Bio import Entrez
Entrez.email = "localuser@localhost.localdomain" 
handle = Entrez.egquery(term="Limnonectes")
record = Entrez.read(handle)

for row in record["eGQueryResult"]:
    print([row["DbName"], row["MenuName"], row["Count"], row["Status"]])