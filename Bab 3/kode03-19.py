from Bio import Entrez
Entrez.email = "localuser@localhost.localdomain" 
acc_no = "X05035"
record = Entrez.read(Entrez.elink(dbfrom = "nuccore", id = acc_no))
linkrec = record[0]["LinkSetDb"][0]["Link"][0]["Id"]
handle = Entrez.efetch(db = "pubmed", id = linkrec, rettype = "abstract", retmode = "text")
print(handle.read())