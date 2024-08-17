import os
from Bio import SeqIO
from pydna.dseqrecord import Dseqrecord
from pydna.amplify import Anneal
from pydna.primer import Primer

dir_kerja = os.getcwd()
FASTA_file = "r%s\FASTA\Oryza sativa 18S rDNA.fasta" % (dir_kerja)

inputSeqFile = open(FASTA_file, "r")
SeqDict = SeqIO.parse(inputSeqFile, "fasta")

PrimerF = "AACTTTCGATGGTAGGATAGGG"
PrimerR = "CGGAATCCTATGATGTTATCCC"

for fasta in SeqDict:
    acc_id = fasta.id
    desc = fasta.description
    sequence = str(fasta.seq)

Template = Dseqrecord(sequence)

Load_PrimerF = Primer(PrimerF)
Load_PrimerR = Primer(PrimerR)
Virtual_Ann_PCR = Anneal([Load_PrimerF, Load_PrimerR], Template)
amplicon_list = Virtual_Ann_PCR.products
amplicon = amplicon_list.pop()
print("Program PCR")
print(amplicon.program())
print("Panjang amplikon:",len(amplicon.seq), "bp")