from Bio import Entrez
Entrez.email = "localuser@localhost.localdomain" 
handle = Entrez.espell(term="Crytodacctylus")
record = Entrez.read(handle)
print(record['Query'], record['SpelledQuery'], record['CorrectedQuery'], record['Database'])