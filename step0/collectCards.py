## 2016-07-05, Constantin Heidegger
## This script collects the datacards in order to be able to run the limits and
## produce the final plots. CAREFUL: This script assumes, that there is a certain
## directory structure in the input directory: <ipath>/<lumi>/<model>/<bkg/mps>/etc.
## as you get by the cmds_scan.py script in heppy.
## command: python collectCards.py

import ROOT, os

# path settings
ipath = "/afs/cern.ch/user/c/cheidegg/www/heppy/2016-07-05_ewk80X_scan_4fb_C1N2LL/"
opath = os.getcwd()

# lumi scenarios
lumis = [
         "4fb",
         #"10fb",
        ]

# signal models to process (if available)
sigs = [
        "TChiNeu_WZ",
        "TChiNeu_WH",
        "TChiNeu_SlepSneu_FD",
        "TChiNeu_SlepSneu_TE",
        "TChiNeu_SlepSneu_TD",
        "TNeuNeu_ZZ",
        "TNeuNeu_HZ",
        "TNeuNeu_HH",
       ]



## ----------- do not touch beyond this line --------------

def cmd(cmd):
	print cmd
	os.system(cmd)

def cp(loc, dest):
	cmd("cp " + loc + " " + dest)

def mkdir(path):
	if os.path.isdir(path): return
	cmd("mkdir " + path)

def mv(loc, dest):
	cmd("mv " + loc + " " + dest)

def rm(loc):
	cmd("rm " + loc)

def replaceInFile(path, search, replace):
	f = open(path, "r")
	lines = "".join(f.readlines())
	f.close()
	lines = lines.replace(search, replace)
	rm(path)
	f = open(path, "w")
	f.write(lines)
	f.close()

def GetKeyNames( self, dir = "" ):
	self.cd(dir)
	return [key.GetName() for key in ROOT.gDirectory.GetListOfKeys()]

ROOT.TFile.GetKeyNames = GetKeyNames

ipath = ipath.rstrip("/") + "/"
opath = opath.rstrip("/") + "/"

mkdir(opath)

for l in lumis:
	if not os.path.isdir(ipath + l): continue
	mkdir(opath + l)
	for s in sigs:
		if not os.path.isdir(ipath + l + "/" + s): continue
		mkdir(opath + l + "/" + s)
			
		thepath = ipath + l + "/" + s + "/mps"
		ls = os.listdir(thepath)

		for mp in ls:
			if not os.path.isdir(thepath + "/" + mp): continue
			cp(thepath + "/" + mp + "/_sig_" + s + "_" + mp + "/SR.card.txt", opath + l + "/" + s + "/" + mp + ".txt")
			cp(thepath + "/" + mp + "/common/SR.input.root"                 , opath + l + "/" + s + "/" + mp + ".root")
			replaceInFile(opath + l + "/" + s + "/" + mp + ".txt", "../common/SR.input.root", opath + l + "/" + s + "/" + mp + ".root")


