from Bio import Entrez
Entrez.email = "localuser@localhost.localdomain" 
acc_no = " X05035"
link = Entrez.elink(dbfrom = "nuccore", id = acc_no)
record = Entrez.read(link)
print(record)