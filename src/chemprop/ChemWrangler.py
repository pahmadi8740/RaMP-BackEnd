'''
Created on Dec 7, 2020

@author: braistedjc
'''
import sys
from rampEntity.Molecule import Molecule


class ChemWrangler(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.chemLibDict = dict()
            
    def readHMDBSDF(self, source, filePath):
        print(sys.getdefaultencoding())
        print("HMDB SDF")
        i = 0
        sdfDB = open(filePath, 'r+', encoding="utf-8")
        molDict = dict()
        mol = Molecule()
        mol.source = source
        
        while True:
            line = sdfDB.readline()

            if len(line) == 0:
                print("line is none...")
                break
            line = line.strip()            
            if line == '$$$$':
                i = i + 1
               # print("processing structure " + str(i))
                molDict[mol.id] = mol
                mol = Molecule()
                mol.source = source
            if line == '> <DATABASE_ID>':
                mol.id = "hmdb:" + sdfDB.readline().strip()
            if line == '> <SMILES>':
                mol.smiles = sdfDB.readline().strip()
            if line == '> <INCHI_KEY>':
                mol.inchiKey = sdfDB.readline().strip()
            if line == '> <INCHI>':
                mol.inchi = sdfDB.readline().strip()                                          
            if line == '> <MOLECULAR_WEIGHT>':
                mol.mw = sdfDB.readline().strip()
            if line == '> <EXACT_MASS>':
                mol.monoisotopicMass = sdfDB.readline().strip()
            if line == '> <GENERIC_NAME>':
                mol.name = sdfDB.readline().strip()

        print("have chem props = " + str(len(molDict)))
        self.chemLibDict[source] = molDict
        
    def readChebiSDF(self, source, filePath):
        print(sys.getdefaultencoding())
        print("ChEBI SDF")

        i = 0
        sdfDB = open(filePath, 'r+', encoding="utf-8")
        molDict = dict()
        mol = Molecule()
        mol.source = source
        while True:
            line = sdfDB.readline()

            if len(line) == 0:
                print("line is none...")
                break
            line = line.strip()            
            if line == '$$$$':
                i = i + 1
               # print("processing structure " + str(i))
                molDict[mol.id] = mol
                mol = Molecule()
                mol.source = source
            if line == '> <ChEBI ID>':
                mol.id = sdfDB.readline().strip()
                mol.id = mol.id.replace("CHEBI", "chebi")
            if line == '> <SMILES>':
                mol.smiles = sdfDB.readline().strip()
            if line == '> <InChiKey>':
                mol.inchiKey = sdfDB.readline().strip()
            if line == '> <InChi>':
                mol.inchi = sdfDB.readline().strip()                                          
            if line == '> <MASS>':
                mol.mw = sdfDB.readline().strip()
            if line == '> <Monoisotopic Mass>':
                mol.monoisotopicMass = sdfDB.readline().strip()
            if line == '> <ChEBI Name>':
                mol.name = sdfDB.readline().strip()

        print("have chem props = " + str(len(molDict)))
        self.chemLibDict[source] = molDict

    def readSDF(self, source, file):
        if source == 'hmdb':
            self.readHMDBSDF(source, file)
        if source == 'chebi':
            self.readChebiSDF(source, file)

    def loadRampChemRecords(self, sources):
        for source in sources:
            if source == 'hmdb':
                file = "C:/Users/braistedjc/Desktop/Analysis/RaMP/RaMP2_Stats/accounting_id_match/chebi_resources/structures.sdf"
                self.readSDF('hmdb', file)
            if source == 'chebi':
                file = "C:/Users/braistedjc/Desktop/Analysis/RaMP/RaMP2_Stats/accounting_id_match/chebi_resources/ChEBI_complete_3star.sdf"
                self.readSDF('chebi', file)
                
    def getChemSourceRecords(self):
        return self.chemLibDict
                                    
# > <INCHI_IDENTIFIER>
# InChI=1S/C4H6O3/c1-2-3(5)4(6)7/h2H2,1H3,(H,6,7)
# 
# > <INCHI_KEY>
# TYEYBOSBBBHJIV-UHFFFAOYSA-N
# 
# > <FORMULA>
# C4H6O3
# 
# > <MOLECULAR_WEIGHT>
# 102.0886
# 
# > <EXACT_MASS>
# 102.031694058



# cw = ChemWrangler()
#         
# file = "C:/Users/braistedjc/Desktop/Analysis/RaMP/RaMP2_Stats/accounting_id_match/chebi_resources/structures.sdf"
# cw.readSDF('hmdb', file)
# 
# file = "C:/Users/braistedjc/Desktop/Analysis/RaMP/RaMP2_Stats/accounting_id_match/chebi_resources/ChEBI_complete_3star.sdf"
# cw.readSDF('chebi', file)

# cw.readSDF('chebi', file)
        
        