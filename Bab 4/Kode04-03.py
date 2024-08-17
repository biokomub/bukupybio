import os 
from Bio import SeqIO

dir_kerja = os.getcwd()
namaFiletarget = r"%s\FASTA\naja.fasta" % (dir_kerja)

fileSekuenInputan = open(namaFiletarget, "r")
fastaSeqDict = SeqIO.parse(fileSekuenInputan, "fasta")

for fasta in fastaSeqDict:
    acc_id = fasta.id
    desc = fasta.description
    sequence = fasta.seq
    print("ID: ", acc_id)
    print("Deskripsi: ", desc)
    print("Sekuen: ", sequence)