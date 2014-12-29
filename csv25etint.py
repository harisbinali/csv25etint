# Script converts CSV formatted file to Tintagel's 5E D&D Card Template (CORE)
# Template can be found at http://rpg.drivethrustuff.com/product/139323/Tintagels-5E-DD-Card-Template-CORE?manufacturers_id=4238
#
# CSV file format is as such:
# "card color";"level";"name";"school";"action";"action icon";"range";"range icon";"components";"duration";"rule text";"overpower"
#
# Command syntax is
# csv25etint -i <CSV file name> -o <output file name> -c <style sheet (usually class name)>

import csv
import zipfile
import os
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--input", dest="csvfilename")
parser.add_option("-o", "--output", dest="msesetfilename")
parser.add_option("-c", "--class", dest="classstylesheet")
(options, args) = parser.parse_args()

fieldnames = ("card color","level","name","school","action","action icon","range","range icon","components","duration","rule text", "overpower")

with open(options.csvfilename, 'r') as csvfile:
	with open('set', 'w') as set:
		reader = csv.DictReader ( csvfile, fieldnames, delimiter = ';', quotechar = '\"' ) 

		set.write("mse version: 0.3.8\n")
		set.write("game: 5E_Tint\n")
		set.write("stylesheet: "+ options.classstylesheet + "\n")

		for row in reader:
			set.write("card:\n")
			set.write("\thas styling: false\n")
			set.write("\tcard color: " + row["card color"] + "\n")
			set.write("\tname: " + row["name"] + "\n")
			set.write("\trule text: " + row["rule text"] + "\n")
			set.write("\toverpower: "  + row["overpower"] + "\n")
			set.write("\tlevel: " + row["level"] + "\n")
			set.write("\tschool: " + row["school"] + "\n")
			set.write("\taction: " + row["action"] + "\n")
			set.write("\taction icon: " + row["action icon"] + "\n")
			set.write("\trange: " + row["range"] + "\n")
			set.write("\trange icon: " + row["range icon"] + "\n")
			set.write("\tcomponents: " + row["components"] + "\n")
			set.write("\tduration: " + row["duration"] + "\n")

with zipfile.ZipFile(options.msesetfilename + ".mse-set", 'w', zipfile.ZIP_DEFLATED) as myzip:
    myzip.write('set')
	
os.remove("set")