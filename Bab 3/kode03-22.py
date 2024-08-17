from Bio import ExPASy
from Bio import SeqIO
handle = ExPASy.get_sprot_raw("Q942F3")
protein_seq_record = SeqIO.read(handle, "swiss")
handle.close()
print(protein_seq_record)