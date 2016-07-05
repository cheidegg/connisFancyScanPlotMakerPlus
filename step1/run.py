## 2016-07-05, Constantin Heidegger
## This script prepares and submits the jobs to run the HiggsCombine tool to get
## the upper limits from a set of datacards in the input directory. This script
## assumes a certain directory structure of the input and the output directories 
## (c.f. step0). The HiggsCombine command is specified in the submit.sh script.
## command: python run.py

import os

# path settings
ipath = os.getcwd().rstrip("step1") + "step0" # output directory of step0 (herein the script searches for the lumi directory)
opath = os.getcwd()                           # output directory of this step
subm  = opath + "/submit.sh"                  # the location of the submission script
cmssw = "/shome/cheidegg/p/CMSSW_7_1_5/src/"  # the path to the SRC of the CMSSW where HiggsCombine is installed 

# batch settings
batch = True # True if you want to run on batch
psi   = True # True if you want to run on psibatch, False for lxbatch

# lumi scenario
lumis = [
         "4fb",
         #"7fb",
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



## ------------ do not touch beyond this line ---------------

def cmd(cmd):
	print cmd
	os.system(cmd)

def cp(loc, dest):
	if not os.path.isdir(dest): mkdir(dest)
	cmd("cp " + loc + " " + dest)

def mkdir(path):
	if os.path.isdir(path): return
	cmd("mkdir -p " + path)

def submit(lumi, sig, file):
	global batch, psi, ipath, opath, cmssw
	op = opath + lumi + "/" + sig + "/"
	oc = cmssw + lumi + "/" + sig + "/"
	mkdir(op)
	mkdir(oc)
	cp(ipath + lumi + "/" + sig + "/" + file, cmssw + lumi + "/" + sig)
	if batch:
		mkdir(opath + lumi + "/" + sig + "/logs")
		f = file.rstrip(".txt")
		super  = "bsub -q 8nh -J combineJob"
		if psi: super = "qsub -q all.q -N combineJob"
		cmd("{SUPER} -o {O}/logs/{F}.log -e {O}/logs/{F}.err {CMSSW}submit.sh {OC} {O} {FILE}".format(SUPER=super, O=op, F=f, CMSSW=cmssw, OC=oc, FILE=file))
	else:
		cmd("source {CMSSW}submit.sh {OC} {O} {FILE}".format(CMSSW=cmssw, OC=oc, O=op, FILE=file))

ipath = ipath.rstrip("/") + "/"
opath = opath.rstrip("/") + "/"
cmssw = cmssw.rstrip("/") + "/"

mkdir(opath)
cp(subm, cmssw)

for l in lumis:
	if not os.path.isdir(ipath + l): continue
	for s in sigs:
		if not os.path.isdir(ipath + l + "/" + s): continue
		ls = os.listdir(ipath + l + "/" + s)
		for mp in ls:
			if mp.find(".txt") == -1: continue
			submit(l, s, mp)


