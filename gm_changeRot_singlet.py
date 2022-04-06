#!/usr/env/bin python
#2021.12.01

#Please calculate the rotation number "194=360*7/13" and edit the script before executing the scipt

from optparse import OptionParser
from os import path
import os

def main():
        usage = """prog [option]\nThis program will rotate the particles by 194 degree\nThe output file contains a _rot194.star suffix."""
        parser = OptionParser(usage=usage)
        parser.add_option("--starfile", dest="starfile", type="string", help="The input file name(*.star)")

        (options, args) = parser.parse_args()
        print usage

	starfile = open(options.starfile, "r").readlines()
	filename = options.starfile

        fp = open("%s_rot194.star" % filename.split(".")[0],  "a")
#       fp.write("\n")
        for line in starfile:
                if len(line.split()) < 15:
                        fp.writelines(line)
			if line.startswith("_rlnAngleRot"):
				IndexAngleRot = int(line.split("#")[1])
			else: continue
                else:
			a = 0.000000
			m = line.split()[IndexAngleRot-1]
			a = float(m)
			if a <= -14:
				b = a + 194
			else:
				b = a + 194 - 360
			for i in range(len(line.split())):
				if IndexAngleRot - i != 1:
					fp.write("%s\t" % line.split()[i])
				else:
					fp.write("%f\t" % b)
		fp.write("\n")
	fp.close()

	print "\nOutput star file is %s_rot194.star" % filename.split(".")[0]

if __name__ == "__main__":
        main()


