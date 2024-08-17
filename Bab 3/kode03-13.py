from Bio import Entrez
Entrez.email = "localuser@localhost.localdomain" 
id_list = ["LC706527", "LC706529", "LC706533", "LC706535", "LC706536", "LC706538"]
post_query = Entrez.epost("nuccore", id=",".join(id_list))
search_results = Entrez.read(post_query)
qkey = search_results["QueryKey"]
web_env = search_results["WebEnv"]
seqs_dumps = Entrez.efetch(db = "nuccore", query_key = qkey, WebEnv = web_env, rettype ="fasta", retmode="text")
print(seqs_dumps.read())