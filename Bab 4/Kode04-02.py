import os
import pathlib 
from Bio import Entrez

Entrez.email = "localuser@localhost.localdomain" 
dir_kerja = os.getcwd()
namaFiletarget = r"%s\FASTA\naja.fasta" % (dir_kerja)
target_dir = os.path.dirname(namaFiletarget)

if os.path.exists(target_dir) == False:
    print("Folder", target_dir, "tidak ada!")
    print("Folder", target_dir, "akan dibuat...")
    pathlib.Path(target_dir).mkdir(parents = True)
    print("Folder", target_dir, "sudah dibuat!")
else:
    print("Folder", target_dir, "sudah ada!")
    pass    
    
if not os.path.isfile(namaFiletarget):
    print("Download file FASTA ke" , namaFiletarget)
    output_file_handle = open(namaFiletarget, "w")
    efetch_handle = Entrez.efetch(db = "nuccore", id = "OM037657", rettype = "fasta", retmode = "text")
    try:  
        output_file_handle.write(efetch_handle.read())
        print("Download FASTA selesai")
        output_file_handle.close()
    except BaseException as be:
        exception_type = type(be).__name__
        print("Ada Error:", exception_type)
    finally:
        output_file_handle.close()
        efetch_handle.close()
else:
    print("Tidak bisa mendownload FASTA!")
    print("Karena file" , namaFiletarget , "ada! ")