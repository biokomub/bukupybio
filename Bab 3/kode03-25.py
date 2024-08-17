import os
import pathlib
from Bio.PDB import PDBList

dir_kerja = os.getcwd()
pdb_dir = r"%s\Model protein" % (dir_kerja)

if os.path.isdir(pdb_dir) == False:
    print("Folder", pdb_dir , "tidak ada!")
    print("Folder", pdb_dir , "harus dibuat...")
    pathlib.Path(pdb_dir).mkdir(parents = True)
    print("Folder", pdb_dir , "sudah dibuat!")
else:
    print("Folder", pdb_dir , "sudah ada...")
    pass

pdbl = PDBList()
pdbl.retrieve_pdb_file("1GZX", pdir = pdb_dir, file_format = "pdb")