"""Setup environment"""
import os, sys, subprocess, re
import numpy as np
import pandas as pd
from glob import glob

def shell(cmd):
	""" Executes a shell command """
	return subprocess.call(cmd, shell = True)

def shellout(cmd):
	""" Saves output of shell command """
	return subprocess.check_output(cmd, shell = True).decode("utf-8").rstrip('\n')

def convert_spaces(var, character):
	""" Removes spaces in string, joined by 'character' """
	if ' ' in var:
		var = (character).join(var.split(' '))
		return var
	else:
		return var

def lines():
	return '-'*70

ans_symbol = r'[,\\({\)[\}\].?;:"\'`!@#$%&*~/^]'



"""Create new directory for analysis
"""

while True:
	clientID = input("Enter client ID:\t")
# TODO: error trap to search for valid client ID in client database

while True: 
	dirname = convert_spaces(input("Enter dir name:\t"),'_')
	if dirname in os.listdir(): 
		print(f'Directory exists \'{dirname}\'. Input a different directory name.\n')
		continue
	elif ( re.search(ans_symbol, dirname) ) or dirname == '': 
		print(f'Invalid input {dirname}. Please try again.\n')
		continue
	else:
		dirname = dirname+'_blastanalysis_'+str(clientID)
		os.mkdir(dirname)
		os.chdir(dirname)
		print(f'{lines()}\nNew directory {dirname} created for blast analysis.\n{lines()}')
		break


""" Specify database type and query type
"""
moltype = {'DNA','PROTEIN'}
while True:
	in_moltypeDB = input("Is database type DNA or protein?\t")
	in_moltypeQuery = input("Is query type DNA or protein?\t")
	if in_moltypeDB.upper() not in moltype and in_moltypeQuery.upper() not in moltype:
		print('Invalid input. Please try again')
		continue
	else:
		print(f'Database type is {in_moltypeDB}\nQuery type is {in_moltypeQuery}\n')
		in_moltypeDB = in_moltypeDB.lower()
		in_moltypeQuery = in_moltypeQuery.lower()


""" Make local database or proceed to query retrieval?
"""

if in_makedb.upper() == 'YES':
	# TODO: in_fastafile to get fasta file input

	# OPTION 1
	# TODO: retrieve sequencees from Eutils search/fetch
	# TODO: in_searchdb to specify which database
	shell(fr'esearch -db {in_searchdb} -query "{in_searchquery}"| efetch -format acc > {in_fastafile}.fasta')
	# TODO: check if query to be used for DB is suitable
		# Use pandas / biopython to filter these sequences

	# OPTION 2
	# TODO: in_remotefilename to specify retrieved fastafile name
	# TODO: in_dburl to get remote sequence url
	shell(fr'wget -O {in_fastafile}.fasta \'{in_dburl}\'')


	# TODO: in_dbname to specify database name

	# Make custom blast database
	shell(fr'makeblastdb -in {in_fastafile} -dbtype {in_moltypeDB} -out {in_dbname}')

else:
	print('Skipping local blast database construction.')


""" Retrieve existing query sequence or search for new sequences?
"""

# TODO: in_existingseq to specify which existing sequence to use


""" Run blast analysis
"""
# TODO: in_blasttype to specify type of blast to run
# TODO: in_queryname to specify query file name
# TODO: in_format to specify format of output file
# TODO: in_outfilename to specify blast output file name
shell(fr'{in_blasttype} -db {in_dbname} -query {in_queryname} -outfmt {in_format} > {in_outfilename}.out')


""" Output blast analysis
"""
# print output to screen for rough quality checking


""" Analyze based on client request
"""
# separate snakemake scripts per each analysis type, using the '.out' file