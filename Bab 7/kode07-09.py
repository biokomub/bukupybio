import os
import pathlib
from dendropy import ProteinCharacterMatrix
from dendropy.interop.raxml import RaxmlRunner
from Bio import Phylo
import matplotlib
from matplotlib import pyplot

RAxML_bin = r"D:\BIOTOOLS\RAxML\raxmlHPC.exe"

dir_kerja = os.getcwd()
NEXUS_file = r"%s\NEXUS\Trimmed COX1 Bovines Protein.nexus" % (dir_kerja)
NEXUS_dir = os.path.dirname(NEXUS_file)
NEWICK_Tree_file = r"%s\Filogeni\ML Protein\COX1 Bovines Protein.nwk" % (dir_kerja)
NEWICK_dir = os.path.dirname(NEWICK_Tree_file)

if os.path.isdir(NEXUS_dir) == False:
    print("Folder", NEXUS_dir, "tidak ada!")
    print("Folder", NEXUS_dir, "harus dibuat...")
    pathlib.Path(NEXUS_dir).mkdir(parents = True)
    print("Folder", NEXUS_dir, "sudah dibuat!")
else:
    print("Folder", NEXUS_dir, "sudah ada...")
    pass

if os.path.isdir(NEWICK_dir) == False:
    print("Folder", NEWICK_dir, "tidak ada!")
    print("Folder", NEWICK_dir, "harus dibuat...")
    pathlib.Path(NEWICK_dir).mkdir(parents = True)
    print("Folder", NEWICK_dir, "sudah dibuat!")
else:
    print("Folder", NEWICK_dir, "sudah ada...")
    pass

if not os.path.isfile(NEWICK_Tree_file):
    print("File Bootstrap Tree", NEWICK_Tree_file, "Belum ada!")
    print("Membuat:", NEWICK_Tree_file)
    BootstrapTreesdata = ProteinCharacterMatrix.get(path = NEXUS_file, schema="nexus")
    rxRun = RaxmlRunner(working_dir_path = NEWICK_dir, raxml_path = RAxML_bin)
    BootstrapTreesRun = rxRun.estimate_tree(BootstrapTreesdata, ["-m", "PROTGAMMAIFLUF", "-N", "1000"])
    BootstrapTreesRun.write(path = NEWICK_Tree_file, schema = "newick")
    print(NEWICK_Tree_file, "selesai dibuat!")
else:
    print("Tidak bisa membuat file Bootstrap Tree!")
    print("Karena file" , NEWICK_Tree_file, "ada!")

#baca dan plot filogeni
Filogeni = Phylo.read(NEWICK_Tree_file, "newick")
matplotlib.rc("font", size = 40)
matplotlib.rc("axes", titlesize = 40)
matplotlib.rc("axes", labelsize = 40)
matplotlib.rc("xtick", labelsize = 40)
matplotlib.rc("ytick", labelsize = 40)
fig = pyplot.figure(figsize = (50, 20), dpi = 300)
axes = fig.add_subplot(1, 1, 1)
Phylo.draw(Filogeni, show_confidence = True, axes = axes)