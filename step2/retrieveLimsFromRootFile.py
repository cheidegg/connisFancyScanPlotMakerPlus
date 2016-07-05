## 2016-07-05, Constantin Heidegger
## This script collects all limits (obs and expected) including error band
## for all mass points of a particular model and lumi scenario and writes it
## into a text file for every model; if more than one lumi scenario is given
## the limits are still put together in the same file but with a header. 

import ROOT, os

## path settings
ipath = os.getcwd().rstrip("step2") + "step1" # output directory of step1 (herein the script searches for the lumi directory)
opath = os.getcwd()                           # output directory of this step

## prepend generated by HiggsCombine
tag  = "higgsCombine" ## prepended to the file name, <TAG><PROCESS NAME>.txt.Asymptotic.Bla.root

## lumi scenario
lumis = [
         "4fb",
         #"10fb",
        ]

## signal model to process (if available)
sigs = [
        "TChiNeu_WZ",
        "TChiNeu_WH",
        "TChiNeu_SlepSneu_FD",
        "TChiNeu_SlepSneu_TD",
        "TChiNeu_SlepSneu_TE",
        "TNeuNeu_ZZ",
        "TNeuNeu_HZ",
        "TNeuNeu_HH",
       ]


## ------------ do not touch beyond this line ---------------

ipath = ipath.rstrip("/") + "/"
opath = opath.rstrip("/") + "/"
lims  = [[[] for l in lumis] for s in sigs]

for i,l in enumerate(lumis):

	if not os.path.isdir(ipath + l): continue
	for si, s in enumerate(sigs):
		if not os.path.isdir(ipath + l + "/" + s): continue
		
		ls = os.listdir(ipath + l + "/" + s)
		for d in ls:
			if d.find(".root") == -1: continue
			if d.find(tag    ) == -1: continue
		
			proc = d.split(".")[0].lstrip(tag)
			mass = proc.split("_")
	
			if os.path.getsize(ipath + l + "/" + s + "/" + d) < 1000: continue

			f = ROOT.TFile.Open(ipath + l + "/" + s + "/" + d)	
			t = f.Get("limit")
			obs=0; exp=0; ep1s=0; em1s=0; ep2s=0; em2s=0
			for ev in t:
				if abs(ev.quantileExpected + 1    ) < 0.02: obs  = ev.limit
				if abs(ev.quantileExpected - 0.5  ) < 0.02: exp  = ev.limit
				if abs(ev.quantileExpected - 0.16 ) < 0.02: em1s = ev.limit
				if abs(ev.quantileExpected - 0.84 ) < 0.02: ep1s = ev.limit
				if abs(ev.quantileExpected - 0.025) < 0.02: em2s = ev.limit
				if abs(ev.quantileExpected - 0.975) < 0.02: ep2s = ev.limit
			f.Close()
			lims[si][i].append((mass[0], mass[1], exp, obs, ep1s, em1s, ep2s, em2s))


for si, s in enumerate(sigs):
	if len(lims[si][0]) == 0: continue 
	f = open(opath + "limits_" + s + ".txt","w")
	
	for i,l in enumerate(lumis):
		if len(lumis) > 1: f.write("limits for lumi: " + l + "\n")
		lims[si][i].sort()
		for y in lims[si][i]:
			f.write("\t".join(str(jj) for jj in y) + "\n")
	
	f.close()
		
	
	
