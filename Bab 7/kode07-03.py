import os
import pathlib
from dendropy.interop.paup import PaupService

PAUP_bin = "D:\\BIOTOOLS\\PAUP4\\paup4c.exe"

dir_kerja = os.getcwd()
NEXUS_file = r"%s\NEXUS\Trimmed COX1 Bovines DNA.nexus" % (dir_kerja)
file_log = r"%s\LOG MODEL\Hasil log.txt" % (dir_kerja)
dir_log = os.path.dirname(file_log)
outgroup = "Tragulus_javanicus_LC060942"
nsekuen = 1545

PAUP_block = """\
    begin paup;
      cd '%s';
      log file = '%s' start;
      execute '%s';
      outgroup '%s';
      nj;
      rateset genes=1:1-%d;
      lset tratio=estimate rmatrix=estimate nst=6 basefreq=estimate rates=siteSpec siterates=rateset:genes shape=estimate pinvar=estimate;
      automodel modelset=j11 aic=yes aicc=yes bic=yes; 
      log stop;
    end
""" % (dir_kerja, file_log, NEXUS_file, outgroup, nsekuen)

if os.path.isdir(dir_log) == False:
    print("Folder", dir_log, "tidak ada!")
    print("Folder", dir_log , "harus dibuat...")
    pathlib.Path(dir_log).mkdir(parents = True)
    print("Folder", dir_log , "sudah dibuat!")
else:
    print("Folder", dir_log , "sudah ada...")
    pass

if not os.path.isfile(file_log):
    print("File Log" , file_log, "Belum ada!")
    print("Membuat:" , file_log)
    returncode, stdout, stderr = PaupService.call(
                paup_commands=PAUP_block,
                paup_path=PAUP_bin,
                cwd = os.getcwd(),
                )
    print(returncode, stdout, stderr)
    print(file_log, "selesai dibuat!")
else:
    print("Tidak bisa membuat file log!")
    print("Karena file" , file_log, "ada!")