#-*-coding: utf-8-*-
from hashlib import md5
from sys import argv
from os import listdir as ls
from os import path
from optparse import OptionParser as op
def add_this_dir_to_filelist(lst = ls()):
	for file in lst:
		if path.isdir(file):
			filelist.append(file)
		else:
			continue
def parse(l):
	with open(l, "r") as h:
		hashes = h.readlines()
	for file in filelist:
		with open(file, "rb") as f:
			if md5(f.read()).hexdigest() in hashes:
				print("**{}'s hash in {}".format(file, l))
if __name__ == '__main__':
	ops = op("USAGE: %prog [args] [values]")
	ops.add_option("-l", "--list", dest="list",default="list.txt",help="Set malware's hashes list.", type="string")
	ops.add_option("-f", "--file",dest="file", default="all in this dir",help="Set what file(s) is(are) going to be check.", type="string")
	(o, argv) = ops.parse_args()
	filelist = []
	if o.file == "all in this dir":
		add_this_dir_to_filelist()
	else:
		filelist.append(o.file)
	parse(o.list)