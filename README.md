connisFancyScanPlotMakerPlus
============================

INSTALLATION
------------
git clone ssh git@github.com:ECOP/connisFancyScanPlotMakerPlus.git connisFancyScanPlotMakerPlus
cd connisFancyScanPlotMakerPlus
git remote add local git@github.com:<YOURNAME>/connisFancyScanPlotMakerPlus.git
git push local master


OVERVIEW
--------
step0: retrieve datacards from wherever heppy has put them
step1: run the higgs combined tool via batch or locally
step2: collect the limits from step1 in a txt file that is to be fed into step 4
step3: produce a histogram of xsec
    a: make a properly formatted text file out of the xsec from the twiki page, to be fed into step 3b
    b: create a ROOT file from the text file in step3b, to be fed into step 4
step4: produce the histograms, smoothing, limit lines, makes a ROOT file to be fed into step5
step5: plot the scan with the official tool


IMPORTANT REMARKS
-----------------
(1) Change your working directory to step0 when running the step0,
to step1 when running step1, etc. The scripts search for the current
working directory, therefore it may lead to weird results when not changing
the working directory properly.
(2) Step5 is the official plotting script. You may consult its readme in order to
be sure of how to run it properly. 
