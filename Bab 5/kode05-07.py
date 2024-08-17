import os
import pathlib
from Bio import SeqIO
from pydna.dseqrecord import Dseqrecord
from pydna.amplify import Anneal
from pydna.primer import Primer
from pydna.gel import gel
from pydna.ladders import GeneRuler_1kb, GeneRuler_1kb_plus, PennStateLadder

dir_kerja = os.getcwd()
FASTA_file = "r%s\FASTA\Oryza sativa 18S rDNA.fasta" % (dir_kerja)
gel_file = "r%s\gambar\gel elektroforesis.png" % (dir_kerja)
gel_dir = os.path.dirname(gel_file)

if os.path.exists(gel_dir) == False:
    print("Folder", gel_dir, "tidak ada!")
    print("Folder", gel_dir, "akan dibuat...")
    pathlib.Path(gel_dir).mkdir(parents = True)
    print("Folder", gel_dir, "sudah dibuat!")
else:
    print("Folder", gel_dir, "sudah ada!")
    pass 

inputSeqFile = open(FASTA_file, "r")
SeqDict = SeqIO.parse(inputSeqFile, "fasta")

PrimerF = "AACTTTCGATGGTAGGATAGGG"
PrimerR = "CGGAATCCTATGATGTTATCCC"

for fasta in SeqDict:
    acc_id = fasta.id
    desc = fasta.description
    sequence = str(fasta.seq)

Template_wDNA = Dseqrecord(sequence)

Load_PrimerF = Primer(PrimerF)
Load_PrimerR = Primer(PrimerR)

Virtual_Ann_PCR = Anneal([Load_PrimerF, Load_PrimerR], Template_wDNA)
amplicon_list = Virtual_Ann_PCR.products
amplicon = amplicon_list.pop()
dseqamplicon = Dseqrecord(amplicon.seq)
gel([GeneRuler_1kb, [], [dseqamplicon]]).save(gel_file, format="png")
print("File disimpan di " , gel_file)