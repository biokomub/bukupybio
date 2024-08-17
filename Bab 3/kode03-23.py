from Bio import ExPASy
handle = ExPASy.get_prosite_raw("PS00262")
text = handle.read()
print(text)
