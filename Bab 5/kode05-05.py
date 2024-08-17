import os
from xml.etree import ElementTree
dir_kerja = os.getcwd()
BLAST_file = r"%s\Hasil BLAST\BLAST Oryza sativa 18s rDNA2.xml" % (dir_kerja)
BLAST_report_handle = open(BLAST_file, "r")

def parseBLASTDefinitions(iteration, banyak_record):
    hitList = list()
    for hit in iteration.findall(".//Hit")[:banyak_record]:
        hitDict = dict()
        for k in ["Hit_def"]:
            hitDict[k] = hit.findtext(k)
        hitList.append(hitDict)
    return hitList

def parseSingleIteration(tree, banyak_record):
    iteration = tree.find(".//Iteration")
    hitList = parseBLASTDefinitions(iteration, banyak_record)
    return hitList

def hitungSeqsfromDefinitions(hitList):
    no_seqs = 0
    for l, hitDict in enumerate(hitL):
        no_seqs += 1
    return no_seqs

def hitungSSfromDefinition(hitList, target_substring):
    no_correct_hits = 0
    for m, hitDict in enumerate(hitL):
        if (target_substring in hitDict["Hit_def"]) == True:
            no_correct_hits += 1
    return no_correct_hits
    
tree = ElementTree.parse(BLAST_file)
hitL = parseSingleIteration(tree, 100)

print("Ada", hitungSeqsfromDefinitions(hitL[:100]), "sekuen dalam BLAST alignment report.")
print("Ada", hitungSSfromDefinition(hitL[:100], "Oryza sativa"), "sekuen yang cocok dengan organisme target.")

BLAST_report_handle.close()