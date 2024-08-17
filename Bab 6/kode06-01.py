import os
import pathlib
from Bio.Align.Applications import ClustalwCommandline

dir_kerja = os.getcwd()
FASTA_file = r"%s\Sekuen\16S Bacteria.fasta" % (dir_kerja)
CLUSTALW_result = r"%s\Hasil Alignment\CLUSTAL\Aln 16S Bacteria.clw" % (dir_kerja)
CLUSTALW_result_dir = os.path.dirname(CLUSTALW_result)

if os.path.isdir(CLUSTALW_result_dir) == False:
    print("Folder" , CLUSTALW_result_dir , "tidak ada!")
    print(CLUSTALW_result_dir , "harus dibuat...")
    pathlib.Path(CLUSTALW_result_dir).mkdir(parents = True)
    print(CLUSTALW_result_dir , "sudah dibuat!")
else:
    print(CLUSTALW_result_dir , "sudah ada...")
    pass

if not os.path.isfile(CLUSTALW_result):
    clustalw_exe = r"D:\BIOTOOLS\ClustalW2\clustalw2.exe"
    cwline = ClustalwCommandline(clustalw_exe, infile = FASTA_file, outfile = CLUSTALW_result, output = "clustal")
    print("Run Command:", cwline)
    stdout, stderr = cwline()
    print(CLUSTALW_result, "berhasil dibuat!")    
    print("Alignment CLUSTALW berhasil!")
else:
    print("Tidak bisa melakukan alignment!")
    print("Karena file" , CLUSTALW_result , "ada!")