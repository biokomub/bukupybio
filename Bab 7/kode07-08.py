import os
import pathlib
from dendropy.interop.paup import PaupService
from Bio import Phylo
import matplotlib
from matplotlib import pyplot

PAUP_bin = r"D:\BIOTOOLS\PAUP4\paup4c.exe"

dir_kerja = os.getcwd()
NEXUS_file = r"%s\NEXUS\Trimmed COX1 Bovines DNA.nexus" % (dir_kerja)
NEXUS_dir = os.path.dirname(NEXUS_file)
NEXUS_BootstrapTrees_file = r"%s\FILOGENI\ML\BTSTRP COX1 Bovines DNA.nexus" % (dir_kerja)
NEWICK_Tree_file = r"%s\FILOGENI\ML\COX1 Bovines DNA.nwk" % (dir_kerja)
NEWICK_dir = os.path.dirname(NEWICK_Tree_file)
outgroup = "Tragulus_javanicus_LC060942"
lset_model = "lset nst=6 rclass=(abacdc) rmatrix=(176.42243 822.57731 176.42243 1 2513.6266) basefreq=(0.28360645 0.26614755 0.16121949) pinv=0.6666426"

PAUP_block = """\
    begin paup;
      cd '%s';
      execute '%s';
      outgroup '%s';
      set criterion=likelihood;
      '%s';
      dset distance=ML; 
      bootstrap search=heuristic nreps=1000 conlevel=50 treefile='%s' format=Nexus /start=stepwise swap=TBR;
    end
""" % (NEXUS_dir, NEXUS_file, outgroup, lset_model, NEXUS_BootstrapTrees_file)

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

if not os.path.isfile(NEXUS_BootstrapTrees_file):
    print("File Bootstrap Tree" , NEXUS_BootstrapTrees_file, "Belum ada!")
    print("Membuat:" , NEXUS_BootstrapTrees_file)
    returncode, stdout, stderr = PaupService.call(paup_commands = PAUP_block, paup_path = PAUP_bin, cwd = os.getcwd())
    print(returncode, stdout, stderr)
    print(NEXUS_BootstrapTrees_file, "selesai dibuat!")
else:
    print("Tidak bisa membuat file Bootstrap Tree!")
    print("Karena file" , NEXUS_BootstrapTrees_file, "ada!")

#Cari pohon konsensus
PAUP_block2 = """\
    begin paup;
      cd '%s';
      execute '%s';
      outgroup '%s';
      set root=outgroup;
      contree all/strict=no majrule=yes treefile='%s' usetreewts=yes saveasrooted=yes format=Newick;
    end
""" % (NEWICK_dir, NEXUS_BootstrapTrees_file, outgroup, NEWICK_Tree_file)

if not os.path.isfile(NEWICK_Tree_file):
    print("File Consensus Tree" , NEWICK_Tree_file, "Belum ada!")
    print("Membuat:" , NEWICK_Tree_file)
    returncode, stdout, stderr = PaupService.call(paup_commands = PAUP_block2, paup_path = PAUP_bin, cwd = os.getcwd())
    print(returncode, stdout, stderr)
    print(NEWICK_Tree_file, "selesai dibuat!")
else:
    print("Tidak bisa membuat file Consensus Tree!")
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