#!/usr/bin/python3

# intro paired data

## making connection between two variables/arrays/lists ie. paired data
## 'key' and 'value' pairs

# creating dicts

{ xxx }

key : values,
key2: values2

eg.
enzymes= {
'EcoRI' : 'GAATC',
'AVAII': 'GGACC'
}

## indexing a dict
enzymes['EcoRI']
motif= enzymes['EcoRI']
print(motif) #GAATC

set(enzymes) # outputs the keys
type(set(enzymes)) # class set
list(set(enzymes)) # outputs the keys
type(list(set(enzymes))) # class list

help(enzymes)
enzymes. #tab #tab

## reset to empty dict
enzymes= {}
enzymes['key'] = 'value'
enzymes['key'] = 'anothervalue' #overrides the value for 'key'
enzymes['key'] = enzymes['key'] + 'value2' # anothervaluevalue2

enzymes.keys() # get keys only
enzymes.values() # get values only
enzymes.items() # get all values in the dict
	dict_items([(ke, values),(key2, value2)])

'key' in enzymes.keys()

## sort dict keys
foo = list(enzymes)
foo.sort()

## retrieve value using a key
enzymes.get('key') # 'value', will return nothing if key doesn't exist

## key
enzymes['5'] = 'somevalue' # key is the string 5
enzymes[5]= 'someothervalue' # key is the integer 5, not actually an index
	# key is always in sq brackets

## indexing via a list
list(enzymes.keys())[2] # a key at index 2
list(enzymes.values())[2] # a value at index 2
list(enzymes.items())[-1] # the item set at the last index

# dic are ordered by insertion order
## used to be in random order
# from collections import OrderedDict
# enzymes=OrderedDict()

## delete/clear
del enzymes['key'] # deletes the entry
enzymes.clear() # clears all entries from the dict
del enzymes # deletes the dict


# counting dinucleotides with a dict
## generate the dinucleotides
dinuc= []
for first in 'ATGC':
	for second in 'ATGC':
		dinuc.append(str(first)+str(second))
## setup dict
all_counts={}
## add entries to dict
for dinuc in dinuc:
	count= dna.upper().count(dinuc)
	# <print statement here>
	all_counts[dinuc] = count

# removing zero counts
nonzero_counts= {}
for dinuc in dinuc:
	howmany= dna.upper().count(dinuc)
	if howmany > 0:
		nonzero_counts[dinuc] = howmany

# specify a default when key is not found
nonzero_counts.get('nonexistentkey',0) # 0 if key doesn't exist


# looping with dictionaries
##eg. which dinuc occur exactly twice
for dinuc in all_counts.keys():
	howmany= all_counts.get(dinuc) # get the value of that dinuc
	if howmany == 2: # if value is equal to 2
		print(dinuc)
##looping over pairs
type(all_counts.items()) # list
for dinuc, howmany in all_counts.items(): # look through the first 'pair' item
	if howmany ==2:
		print(dinuc)

## lookup (.get) vs iteration (loop)

#--------exercises

#!/usr/local/bin/python3
import os
os.system('clear') #---clears the screen

user_info_dict={}

def user_info(idnumber):
	if idnumber == 1:
		user_info_dict['user_id']=idnumber
		user_info_dict['user_name']=input("What is your name?\n\t")
		user_info_dict['user_age']=input("How old are you?\n\t")
		user_info_dict['fave color']=input("What is your favorite color?\n\t")
		user_info_dict['likes python']=input("Do you like Python? yes/no/maybe\n\t")
		user_info_dict['flat earther']=	input("The world is flat: True or False?\n\t")
	else:
		user_info_dict['user_id']= user_info_dict['user_id']+','+idnumber
		user_info_dict['user_name']=  user_info_dict['user_name']+','+input("What is your name?\n\t")
		user_info_dict['user_age']= user_info_dict['user_age']+','+input("How old are you?\n\t")
		user_info_dict['fave color']= user_info_dict['fave color']+','+input("What is your favorite color?\n\t")
		user_info_dict['likes python']= user_info_dict['likes python']+','+input("Do you like Python? yes/no/maybe\n\t")
		user_info_dict['flat earther']= user_info_dict['flat earther']+','+input("The world is flat: True or False?\n\t")
	if 'True' in  user_info_dict.get('flat earther'):
		print("I'm sorry we can't be friends")
	return user_info_dict.item()


#-----exercise_2
gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

def dna_translation(dnaseq, frame=1):
	if type(dnaseq) != str:
		print("DNA sequence must be of type string\nExiting..."); return
	if (type(int(dnaseq)) == int) is True:
		print("DNA sequence must be made up of letters only\nExiting..."); return
	if frame not in [-3,-2,-1,1,2,3]: #---test for valid frame numbers
		print("invalid frame range < -3,-2,-1,1,2,3 >\nExiting..."); return
	dnaseq= dnaseq.upper()
	if frame in [-3,-2,-1]: #---make reverse comp. if frame is -ve
		rc_dna= dnaseq.replace("G","c").replace("A","t").replace("C","g").replace("T","a").upper()[::-1]
		dnaseq= rc_dna
	rc= frame in [-3,-2,-1]
	framestart= abs(frame)-1 #---get index number for frame start
	lastcodon_start= len(dnaseq)-2 #---start position of final codon
	protein= "" #---contains final protein sequence
	for start in list(range(framestart, lastcodon_start, 3)): #---process in three-base chunks
		codon= dnaseq[start:start+3] #---get the codon in uppercase
		aa= gencode.get(codon, "X") #---get the aminoacid when use codon as key, output "X" if codon invalid
		protein= protein + aa #---build protein as aa sequence
	return print("Input sequence:\n\t",dnaseq.upper(),"\nReading frame:\n\t",frame,"\nReverse complement?\n\t",rc,"\nProtein sequence:\n\t",protein)
