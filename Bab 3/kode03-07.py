from Bio import Entrez
Entrez.email = "localuser@localhost.localdomain"
handle = Entrez.einfo(db="nuccore")
db_record = Entrez.read(handle)
for field in db_record["DbInfo"]:
    print(field)