import os
import pathlib
from Bio.KEGG.REST import *
from Bio.KEGG import Enzyme

dir_kerja = os.getcwd()
ke_dir = r"%s\enz2" % (dir_kerja)
ke_file = r"%s\enz.txt" % (ke_dir)
request = kegg_get("ec:1.14.14.179")

if os.path.isdir(ke_dir) == False:
    print("Folder", ke_dir , "tidak ada!")
    print("Folder", ke_dir , "harus dibuat...")
    pathlib.Path(ke_dir).mkdir(parents = True)
    print("Folder", ke_dir , "sudah dibuat!")
else:
    print("Folder", ke_dir , "sudah ada...")
    pass

open(ke_file, 'w').write(request.read())
records = Enzyme.parse(open(ke_file))
record = list(records)[0]
print(record)