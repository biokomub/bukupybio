import os
import pathlib
from Bio.Blast.NCBIWWW import qblast
dir_kerja = os.getcwd()
FASTA_file = r"%s\FASTA\Oryza sativa 18s rDNA.fasta" % (dir_kerja)
BLAST_file = r"%s\Hasil BLAST\BLAST Oryza sativa 18s rDNA.xml" % (dir_kerja)
BLAST_dir = os.path.dirname(BLAST_file)
PrimerF = "AACTTTCGATGGTAGGATAGGG"

fasta_seq = open(FASTA_file).read()

if os.path.exists(BLAST_dir) == False:
    print("Folder", BLAST_dir, "tidak ada!")
    print("Folder", BLAST_dir, "akan dibuat...")
    pathlib.Path(BLAST_dir).mkdir(parents = True)
    print("Folder", BLAST_dir, "sudah dibuat!")
else:
    print("Folder", BLAST_dir, "sudah ada!")
    pass    

if not os.path.isfile(BLAST_file):  
    print("Menulis hasil BLAST ke:", BLAST_file)
    
    PROGRAM = "blastn"
    DATABASE = "nr"
    SEQUENCE = PrimerF
    BLAST_handle = qblast(
                          PROGRAM, 
                          DATABASE, 
                          SEQUENCE,
                          hitlist_size = 100,
                          megablast = False
                          )

    try:
        with open(BLAST_file,"w+") as BLAST_result:
            BLAST_result.write(BLAST_handle.read())
            BLAST_result.close()
    except BaseException as be:
        exception_type = type(be).__name__
        print("Ada Error:", exception_type)
    finally:
        BLAST_handle.close()
        print("BLAST selesai.")
        print("Cek hasil BLAST di:",  BLAST_file)
else:
    print("Tidak bisa mendownload BLAST")
    print("Karena file", BLAST_file, "ada!")