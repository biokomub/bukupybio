from Bio.KEGG.REST import *
request = kegg_info("kegg") 
print(request.read())