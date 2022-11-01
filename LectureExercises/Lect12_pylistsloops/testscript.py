#!/usr/bin/python3
import os, subprocess, string, glob
os.listdir()

#-----EXERCISE1-----#

# copy local files
os.system("cp /localdisk/data/BPSM/Lecture12/*.dna .")
os.system("cp /localdisk/data/BPSM/Lecture12/*.txt .")
os.listdir() # check the files

# ANSWER
input_txt_contents = open('input.txt').read().upper().replace('ATTCGATTATAAGC','').split()
cleanseqs = open('Cleaned_sequences.txt','w')
for cleanones in input_txt_contents2 :
	cleanseqs.write(cleanones[14 :] + '\n')
	cleanones[14 :]
	cleanseqs.close()

# ANSWER2:
with open('input.txt') as mylines :
	my_file_contents = mylines.read().upper().split()
	with open('Cleaned_sequences.txt','w') as cleanedseqs :
		for cleanones in my_file_contents :
			cleanedseqs.write(cleanones[14:] + '\n')
			f'{cleanones[14 :]}'


#-----EXERCISE2-----#
exonslist= open("exons.txt").read().rsplit()
exonslist
genomicdna2= open("genomic_dna2.txt").read().upper()
genomicdna2

with open('Ex2_codingsequence.fasta','w') as coding: # open a pipe to write output
	coding.write('>Lecture12_exercise2_codingseq\n') # insert a fasta header line to output file

counter=0
with open('Ex2_codingsequence.fasta','a') as coding:
	for exons in exonslist:
		counter+=1
		startexon= int(exons.split(',')[0])-1 # get index of start of exon
		endexon= int(exons.split(',')[1]) # get index of end of exon
		exonwanted= genomicdna2[startexon:endexon]
		coding.write(exonwanted)
		regionsummary= 'Exon'+str(counter)+' '+str(exons)+' runs from index position '+str(startexon)+' upto but not including '+str(endexon)+'.'
		print(regionsummary, '\n\t', exonwanted)

coding.closed
print(open('Ex2_codingsequence.fasta').read()


#-----EXERCISE3-----#

os.system("cp ~/LectureExercises/Lect_11/remote_exon01.fasta .") # import sequence file from previous lecture

# segment length= 30bp, windowoffset= 3bp

inputseq= open('remote_exon01.fasta').read().split()[1]
len(inputseq)

windowsize=30
offset=3
segmentstart= list(range(0,len(inputseq)-windowsize+1,offset)) #generates numeric range for window start positions
tempfastaheader= '_window'+str(windowsize)+'_offset'+str(offset) #object takes all the segment sequences

outfilename= 'AJ223353_coding_all'+tempfastaheader+'.fasta' #name of output file
with open(outfilename, 'w') as allsegments:
	allsegments.write('')
	segments_made= [] #blank list holds the segments
	fileswanted= 1 #a switching variable for yes/no option
	for seg_bits in segmentstart:
		#index the input sequence by segment numbers, as uppercase
		tempseq= inputseq[seg_bits:seg_bits+windowsize].upper()
		segments_made= segments_made+[tempseq]
		# %GC content of each segment, convert float to int
		tempGC= int(100*(tempseq.count('G')+tempseq.count('C'))/len(tempseq))
		# make fasta header line
		description= 'AJ223353_coding_'+str(len(segments_made))+'_'+tempseq+tempfastaheader
		fastaheader= '>'+description
		print(len(segments_made),'\t',tempseq,'\t',tempGC)
		# ask if files wanted.
		if fileswanted == 1:
		# open the segment fastafiles
			with open(description+'.fasta', 'w') as segmentfile:
				segmentfile.write(fastaheader+'\n'+tempseq)
				allsegments.write(fastaheader+'\n'+tempseq+'\n\n')
		else:
			allsegments.close()

#-----EXERCISE4-----#

#LINUX:
mkdir dna_files
mv *.dna dna_files/

# get list of files to process:
for filename in os.listdir('dna_files/'):
	if filename.endswith('.dna'):
		f'In file {filename}'
		dna_file= open('dna_files/'+filename)
		# get length of each line for the dna file
		for line in dna_file:
			dna= line.rstrip('\n')
			length= len(dna)
			print(f'\tThis line has dna seq with length {str(length)}')

# to check which bin each sequence (per file) would fit in
for filename in  sorted(os.listdir('dna_files')) : 
	# Check if the file name ends with .dna
	if filename.endswith('.dna') : 
		print('Reading sequences from ' + filename) 
		# Open the file and process each line
		dna_file = open('dna_files/' + filename) 
		# Calculate the sequence length 
		for line in dna_file :
			dna = line.rstrip('\n') 
			length = len(dna) 
			print('\tsequence length is ' + str(length)) 
			# Go through each size bin and check if the sequence belongs in it
			for bin_lower in list(range(100,1000,100)) : 
				bin_upper = bin_lower + 99 
				if length >= bin_lower and length <= bin_upper :
					print('\t\tbin is ' + str(bin_lower) + ' to ' + str(bin_upper)

# create new directory for each size bin
for bin_lower in list(range(100,1000,100)):
	bin_upper= bin_lower+99
	bin_directory_name= str(bin_lower)+'_'+str(bin_upper)
	os.mkdir(bin_directory_name)

# variable holds arbitrary sequence id number
seq_number= 1

# action time
for filename in os.listdir('dna_files/'):
	#only for filenames with .dna
	if filename.endswith('.dna'):
		# open file and process each line
		dna_file= open('dna_files/'+filename)
		for line in dna_file:
			#calculate sequence length
			dna= line.rstrip('\n')
			length= len(dna)
			#check if seq fits in the bins
			for bin_lower in list(range(100,1000,100)):
				bin_upper= bin_lower+99
				if length >= bin_lower and length <= bin_upper:
					bin_dirname= str(bin_lower)+'_'+str(bin_upper)
					# define output file pathname
					out_path= bin_dirname+'/'+str(seq_number)+'.dna'
					output= open(out_path, 'w')
					output.write(dna)
					output.close()
					seq_number = seq_number+1
