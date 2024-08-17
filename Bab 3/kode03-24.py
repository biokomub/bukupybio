from Bio import ExPASy
handle = ExPASy.get_prodoc_entry('PDOC00235')
text = handle.read()
print(text)