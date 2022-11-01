#!/usr/bin/python3

import string, os, shutil, subprocess

data= open('data.csv').read().split('\n')

# Question 1
## gene names for all genes from D.melanogaster or D.simulans
counter=1
for line in data:
 line= line.split(',')
 species= line[0]
 geneseq= line[1].upper()
 seqlength= len(geneseq)
 genename= line[2]
 explevel= int(line[3])	
 ## print(species, geneseq, seqlength, genename, explevel)
 # at content calculations
 atcontent= (geneseq.count("A") + geneseq.count("T"))/seqlength
 atstatus= "low" # this is the default status
 if (atcontent >= 0.45 and atcontent <= 0.65):
  atstatus="medium"
 if (atcontent>0.65):
  atstatus="high"
 # answer all questions for each sequence
 print(counter)
 print(species,",", genename)
 if species == 'Drosophila melanogaster' or species == 'Drosophila simulans':
  print("Question 1:", genename, "gene is present")
 else:
  print("Question 1: failed")
 if seqlength > 90 and seqlength < 110:
  print("Question 2: Gene", genename, "is", seqlength, "bases long")
 else:
  print("Question 2: failed")
 if atcontent < 0.5 and explevel > 200:
  print("Question 3:", genename, "has AT content", atcontent, "and expression level", explevel)
 else:
  print("Question 3: failed")
 if (genename.startswith("k") or genename.startswith("h")) and species != "Drosophile melanogaster":
  print("Question 4: gene", genename, "begins with either the letter 'k' or 'h'")
 else: 
  print("Question 4: failed")
 print("Question 5:", genename, "AT content level is", atstatus, "\n")
 counter += 1


# Question 2
## print all the k-mers of length k, that occur more than n times
#kmer_sizes= list(range(2,int(len(dna)-1)))
kmer_sizes= list(range(2,5))
number_of_times_min= 3
dna= "atatatatatcgcgtatatatacgactatatgcattaattatagcatatcgatatatatatcgatattatatcgcattatacgcgcgtaattatatc"

for window in kmer_sizes:
 kmersfound= []
 kmerrange= list(range(0,len(dna)))
 # then get the kmer sequences
 for firstbase in kmerrange:
  if (firstbase+window)<len(dna)+1:
   seqout= (dna)[firstbase:firstbase+window]
   kmersfound= kmersfound + [seqout]
 # get frequencies of non-redundant set 
 uniqueset= list(set(kmersfound))
 for frequencies in uniqueset:
  freq_count= kmersfound.count(frequencies)
  if freq_count > number_of_times_min:
   print(frequencies, freq_count, "<passed")
  else:
   print(frequencies, freq_count)

# Question 3
## Find similarity between two sequences
## Calculate and print % of identical positions
sequences= ['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']

	# Generate shorter seqs
seq4= sequences.pop()
seq3= sequences.pop()
seq2= sequences.pop()
seq1= sequences.pop()

for bases in seq1:
	counter= 0
	nextdna= ind
	for base in dna:
		if baseinseq1 == baseinseq2:
			counter +=1
			print(#the index of the base		 




