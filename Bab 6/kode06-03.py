import os
import pathlib
from Bio.Align.Applications import MafftCommandline

dir_kerja = os.getcwd()
FASTA_file = r"%s\Sekuen\16S Bacteria.fasta" % (dir_kerja)
MAFFT_result = r"%s\Hasil Alignment\MAFFT\Aln 16S Bacteria.fasta" % (dir_kerja)
MAFFT_result_dir = os.path.dirname(MAFFT_result)

if os.path.isdir(MAFFT_result_dir) == False:
    print("Folder" , MAFFT_result_dir , "tidak ada!")
    print(MAFFT_result_dir , "harus dibuat...")
    pathlib.Path(MAFFT_result_dir).mkdir(parents = True)
    print(MAFFT_result_dir , "sudah dibuat!")
else:
    print(MAFFT_result_dir , "sudah ada...")
    pass

if not os.path.isfile(MAFFT_result):
    MAFFT_exe = r"D:\BIOTOOLS\MAFFT-win\mafft.bat"
    m_line = MafftCommandline(MAFFT_exe, input = FASTA_file, auto = True)
    print("Run Command:", m_line)
    stdout, stderr = m_line()
    with open(MAFFT_result, "w") as handle:
        handle.write(stdout)
    print(MAFFT_result, "berhasil dibuat!")
    print("Alignment MAFFT berhasil!")
else:
    print("Tidak bisa melakukan alignment!")
    print("Karena file" , MAFFT_result , "ada!")