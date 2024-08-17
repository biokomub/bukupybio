from Bio import Entrez
Entrez.email = "localuser@localhost.localdomain" 
id_list = ["LC706527", "LC706529", "LC706533", "LC706535", "LC706536", "LC706538"]
print(Entrez.epost("nuccore", id=",".join(id_list)).read())