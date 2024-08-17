from Bio.KEGG.REST import *
request = kegg_get("ec:1.14.14.179")
print(request.read())