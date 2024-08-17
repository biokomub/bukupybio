import os
import pathlib
import dendropy

dir_kerja = os.getcwd()
FASTA_file = r"%s\TRIMMED SEQS\Trimmed COX1 Bovines DNA.fasta" % (dir_kerja)
NEXUS_file = r"%s\NEXUS\Trimmed COX1 Bovines DNA.nexus" % (dir_kerja)
NEXUS_dir = os.path.dirname(NEXUS_file)

if os.path.isdir(NEXUS_dir) == False:
    print("Folder", NEXUS_dir , "tidak ada!")
    print("Folder", NEXUS_dir , "harus dibuat...")
    pathlib.Path(NEXUS_dir).mkdir(parents = True)
    print("Folder", NEXUS_dir , "sudah dibuat!")
else:
    print("Folder", NEXUS_dir , "sudah ada...")
    pass

if not os.path.isfile(NEXUS_file):
    SeqData = dendropy.ProteinCharacterMatrix.get(path = FASTA_file, schema = "fasta")
    SeqData.write(path = NEXUS_file, schema = "nexus")
    print("File", FASTA_file, "telah dikonversi ke", NEXUS_file )
else:
    print("Tidak bisa membuat file NEXUS!")
    print("Karena file" , NEXUS_file, "ada!")