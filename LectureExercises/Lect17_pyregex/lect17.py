"""
REGEX
"""

	# Finding strings
str.find('thingtofind') # outputs the index

	# import regex
import re

	# re.search()  like boolean
re.search(pattern, string)	# returns a nonetype: either True or None

if re.search(r'pattern', string):
	print(something)
else:
	print(something)


	# search 'OR'	
if re.search(r'G(A|T)CG', string):
	print
else:
	print

if re.search(r'GC(A|T|G|C)GC', string):

if re.search(r'GC[GATC]GC', string)


	# search things that are NOT, in a subset
if re.search(r'[^GATC]', string[index]):
	print
else:
	print


	# characters
\	Escape special character or start a sequence.
.	Match any character except newline
^	Match start of the string		^G = GATC not AGATC
$	Match end of the string			C$ = GATC not GATCA
[]	Enclose a set of matchable characters
()	Create capture group, & indicate precedence

{m}	Exactly m repetitions
{m,n}	From m (default 0) to n (default infinity) repetitions 		eg. GCA{2,4}Y allows 2-4 As
*	0 or more. Same as {,}	thing preceding can be optional, but can also be repeated
+	1 or more. Same as {1,}	thing preceding it can be repeated more than once
?	0 or 1. Same as {,1} 	thing preceding it is optional

\A	Start of string
\b	Match empty string at word (\w+) boundary
\B	Match empty string not at word boundary
\d	Digit
\D	Non-digit
\s	Whitespace [ \t\n\r\f\v]
\S	Non-whitespace
\w	Alphanumeric: [0-9a-zA-Z_]
\W	Non-alphanumeric
\Z	End of string

\a	ASCII Bell (BEL)
\f	ASCII Formfeed
\n	ASCII Linefeed
\r	ASCII Carriage return
\t	ASCII Tab
\v	ASCII Vertical tab
\\	A single backslash


	# make raw string
rawstring= r'hello\nworld\t' 	# prints: hello\nworld\t
rawstring2= r'\n' 	# prints: \n 	# value: '\\n'
rawstring3= r'\\n'	# prints: \\n	# value: '\\\\n'

	
	# STARTS with A or G and ends with C
if re.search(r'^[AG]', 'TGTC') and re.search(r'C$', 'TGTC'):

	# Starts with A or G OR ends with T?
if re.search(r'^[AG]', 'TGTC') or re.search(r'T$', 'TGTC'):


	# CREATE a match object
	# search non-GATC base
match_obj = re.search(r'[^GATC]', dna)
if match_obj :    # if it was "True"
    print('Ambiguous base found!')
    ambig = match_obj.group()
    print('The base is ' + ambig)

	# search for at
match_obj2 = re.search(r'[AT]', dna)
match_obj2.group()	# BUT HOW TO COUNT?
match_obj. #tabtab


	# multiple groups
.+ .+

(.+) (.+)

	# parsing genus and species from list of animals
for this_animal in lots_of_animals :
   new_match_obj = re.search('(.+) (.+)',this_animal)
   if new_match_obj :	# output for True
     print(this_animal + ': genus is ' + new_match_obj.group(1) + ', species is ' + new_match_obj.group(2))
   else :		# error trap that allows failure for None
     print('Unable to find a full genus and species pair for ' + this_animal)

re.search('(.+)(Y)(.+)',dna).group(0)	# prints the input
re.search('(.+)(Y)(.+)',dna).group(1)	# bit 1
re.search('(.+)(Y)(.+)',dna).group(2)	# bit 2 (Y) - what we looked for
re.search('(.+)(Y)(.+)',dna).group(3)	# bit 3


	# THIS IS A HOT MESS

#--------EXERCISES-----------#
import os, sys, subprocess
import pandas as pd
import re
import numpy as np

	# create a list of acc numbers
acc= ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']

for i in np.arange(0,len(acc)):
	match_obj_num5= re.search(r'5', acc[i])	# contain number 5
	if match_obj_num5:
		print('Question 1: Accession {} contains {}'.format(acc[i],num))
	else:
		print('Question 1: Number 5 not found in {}'.format(acc[i]))
	
	match_obj_DorE= re.search(r'[de]', acc[i])      # contain D or E
        if match_obj_DorE:
                print('Question 2: Accession {} contains letter d or e'.format(acc[i]))
        else:
                print('Question 2: d or e not found in {}'.format(acc[i]))
	
	match_obj_DandEorder= re.search(r'de', acc[i])	# contain D and E in order
	if match_obj_DandEorder:
		print('Question 3: Accession {} has d before e'.format(acc[i]))
	else:
		print('Question 3: d not before e in {}'.format(acc[i]))

	match_obj_DandEordersing= re.search(r'd.*e', acc[i])	# D and E in order, single between
	if match_obj_DandEordersing:
		letter= match_obj_DandEordersing.group()
		print('Question 4: Accession {} has letter {} between d and e'.format(acc[i],letter))
	else:
		print('Question 4: No letter between d and e in {}'.format(acc[i]))

	re.search(r'd.e', acc) 	# d and i in order, with single letter

	re.search(r'd',acc) and re.search(r'e',acc)
	
	WRONG match_obj_DandErandom= re.search(r'[d][e]', acc[i])		# D and E in any order
	if match_obj_DandErandom:
		print('Question 5: Accession {} has letter d and e in random order'.format(acc[i]))
	else:
		print('Question 5: Either d or e is not in {}'.format(acc[i]))

	match_obj_swXorY= re.search(r'^[xy]', acc[i])	# starts with x or y
	match_obj_ewE= re.search(r'[e$]', acc[i])	# ends with e
	
	if re.search('(^x|^y).+e$',acc) :
	if re.search('"[xy].+e$',acc) :
	
	if match_obj_swXorY:
		print('Question 6: Accession {} starts with x or y'.format(acc[i]))
	else:
		print('Question 6: Does not start with x or y for {}'.format(acc[i]))

	if match_obj_swXorY and match_obj_ewE:
		print('Question 7: Accession {} starts with x or y and ends with e'.format(acc[i]))
	else:
		print('Question 7: Does not either start with x or y/ not end with e for {}'.format(acc[i]))


	if len(re.findall(r'\d',acc)) == 3 :

	match_obj_any3num= re.search(r'[\d\d\d]', acc[i])	# contains any 3 numbers in any order
	if match_obj_any3num:
		any3num= match_obj_any3num.group()
		print('Question 8: Accession {} has 3 numbers {} throughout'.format(acc[i],any3num))
	else:
		print('Question 8: Less than 3 or no numbers in accession {}'format(acc[i]))

	if len(set(re.findall(r'\d',acc))) == 3 :

	match_obj_3diffnum= re.search(r'', acc[i])	# contains 3 diff numbers
	if match_obj_3diffnum


# contain three or more numbers in a row
if re.search(r'\d{3,}', acc):
if re.search(r'[0123456789]{3,}', acc) :

# end with d followed by either a, r or p
if re.search(r'd[arp]$', acc):

########### OR USE DICTIONARIES #############



subprocess.call("cp /localdisk/data/BPSM/Lecture17/long_dna.txt .", shell=True)
long_dna= open("long_dna.txt").read().rstrip('\n')

	# print format on screen
print("\n".join(re.findall('.{1,60}', dna)))

BpsmI= 'ANT*AAT'.split('*')
	# write a pattern
BpsmI= 'A[GATC]TAAT'


BpsmII= 'GCRW*TG' 

re.search(BpsmI[0]+'$^'+BpsmI[1], long_dna)
