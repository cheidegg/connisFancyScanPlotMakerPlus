## 2016-07-05, Constantin Heidegger
## This script reformats the text file you get when copy-pasting 
## cross section values for different sparticle masses from the twiki.
## Branching fractions or other correction factors can be given with a flag
## e.g. C1N2: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVn2x1wino#Envelope_of_CTEQ6_6_and_MSTW2008
## e.g. N2N3: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVhino (first table) 
## command: python reformat.py <fileWithXSFromTwiki> [<factorToScaleXSWith>]
import sys

factor = 1.
if len(sys.argv) >= 3:
	factor = float(sys.argv[2])

f = open(sys.argv[1], "r")
lines = [l.rstrip("\n") for l in f.readlines()]
f.close()

f = open(sys.argv[1].rstrip(".txt") + "_reformatted.txt", "w")
for l in lines:
	ls = [ll.strip() for ll in l.split("\t")]
	f.write(ls[0] + " GeV " + str(float(ls[1])*factor/1000) + " +/- " + str(float(ls[2])/float(ls[1])) + "%\n")
f.close()
