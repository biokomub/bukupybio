import os
from Bio import SeqIO
import primer3

dir_kerja = os.getcwd()
FASTA_file = r"%s\FASTA\Oryza sativa 18S rDNA.fasta" % (dir_kerja)

inputSeqFile = open(FASTA_file, "r")
SeqDict = SeqIO.parse(inputSeqFile, "fasta")

for fasta in SeqDict:
    acc_id = fasta.id
    desc = fasta.description
    sequence = str(fasta.seq)

primer_list = primer3.bindings.designPrimers(
            {
                "SEQUENCE_ID": "Oryza sativa 18S rRNA gene",
                "SEQUENCE_TEMPLATE": sequence,
                "SEQUENCE_EXCLUDED_REGION": [0, 0] 
            },
            {
                "PRIMER_TASK": "generic",
                "PRIMER_PICK_LEFT_PRIMER": 1,
                "PRIMER_PICK_RIGHT_PRIMER": 1,
                "PRIMER_NUM_RETURN": 5,
                "PRIMER_OPT_SIZE": 22,
                "PRIMER_MIN_SIZE": 18,
                "PRIMER_MAX_SIZE": 30,
                "PRIMER_OPT_TM": 55.0,
                "PRIMER_MIN_TM": 52.0,
                "PRIMER_MAX_TM": 58.0,
                "PRIMER_MIN_GC": 45.0,
                "PRIMER_MAX_GC": 65.0,
                "PRIMER_MAX_POLY_X": 4,
                "PRIMER_GC_CLAMP": 3,
                "PRIMER_MAX_END_GC": 3,
                "PRIMER_PRODUCT_SIZE_RANGE": [200, 1000],
                "PRIMER_TM_FORMULA" : 1,
                "PRIMER_SALT_CORRECTIONS" : 1
            }
            )
#print(primer_list.items())
for key in primer_list:
    print(key, ":", primer_list[key])