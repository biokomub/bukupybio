import os
import pathlib 
from Bio.Blast.NCBIWWW import qblast

dir_kerja = os.getcwd()
namaFileFASTA =  r"%s\FASTA\naja.fasta" % (dir_kerja)
namaFileBLAST = r"%s\Hasil BLAST5\BLAST naja.xml" % (dir_kerja)
target_dir = os.path.dirname(namaFileBLAST)

if os.path.exists(target_dir) == False:
    print("Folder", target_dir, "tidak ada!")
    print("Folder", target_dir, "akan dibuat...")
    pathlib.Path(target_dir).mkdir(parents = True)
    print("Folder", target_dir, "sudah dibuat!")
else:
    print("Folder", target_dir, "sudah ada!")
    pass

if os.path.exists(namaFileBLAST) == False:
    FASTAseq = open(namaFileFASTA).read()
    print("Menulis hasil BLAST ke:", namaFileBLAST)            
    PROGRAM = "blastn"
    DATABASE = "nr"
    SEQUENCE = FASTAseq
    BLAST_handle = qblast(PROGRAM, DATABASE, SEQUENCE, hitlist_size = 5, megablast = False)
    try:
        with open(namaFileBLAST, "w+") as BLAST_result:
            BLAST_result.write(BLAST_handle.read())
            BLAST_result.close()
    except BaseException as be:
        exception_type = type(be).__name__
        print("Ada Error:", exception_type)
    finally:
        BLAST_handle.close()
        print("BLAST selesai.")
        print("Cek hasil BLAST di:", namaFileBLAST)
else:
    print("BLAST tidak dilakukan karena file", namaFileBLAST, "ada!")