#!/usr/bin/bash

#----LINUX----#
subprocess.call("cp /localdisk/data/BPSM/Lecture11/plain_genomic_seq.txt   . ",shell=True)
# get the remote sequence
wget -qO AJ223353.fasta "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AJ223353&rettype=fasta&retmode=text"| grep -v ">" > AJ223353_noheader.fasta
		## alternatively use edirect
		# esearch -db nucleotide -query "AJ223353[accession]" | efetch -db nucleotide -format fasta | grep -v ">" > AJ223353_noheader.fasta

		## genbank standard format
		# wget -qO AJ223353.genbank "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AJ223353&rettype=gb&retmode=text"
		# esearch -db nucleotide -query "AJ223353[accession]" | efetch -db nucleotide -format gb > AJ223353.genbank

## extract just the CDS (coding segment)
esearch -db nucleotide -query "AJ223353[accession]" | efetch -db nucleotide -format gb | grep "CDS"
#---- END OF LINUX----#



#!/usr/bin/python3

import os, subprocess, shutil

## copy local dna sequence
subprocess.call("cp /localdisk/data/BPSM/Lecture11/plain_genomic_seq.txt   . ",shell=True)
	# os.system("cp /localdisk/data/BPSM/Lecture11/plain_genomic_seq.txt   .")
	# shutil.copy("/localdisk/data/BPSM/Lecture11/plain_genomic_seq.txt","./shutilversion.txt")

os.listdir()
print("\n".join(os.listdir()))


# open and read remote file, convert to upper case
remotefile = open("AJ223353_noheader.fasta").read().upper()
len(remotefile)
	#convert to single line
remotefile_singleline = remotefile.replace("\n","")
remotefile_singleline_ready = remotefile_singleline # prep copy for other analyses
	# rmeove non-DNA chars
remotefile_singleline_anythingleft = remotefile_singleline.replace("G","").replace("A","").replace("T","").replace("C","")
	# coding-noncoding, bases 29..409. the rest is not protein coding
remote_noncoding01 = remotefile_singleline_ready[0:28]
remote_exon01 = remotefile_singleline_ready[28:409]
remote_noncoding02 = remotefile_singleline_ready[409:]
	# write out the files, sequentially
		# remote noncoding
remote_noncoding01_out = open("remote_noncoding01.fasta", "w")
remote_noncoding01_out.write(">AJ223353_noncoding01_length" + str(len(remote_noncoding01)) + "\n")
remote_noncoding01_out.write(remote_noncoding01)
remote_noncoding01_out.close()
print(open("remote_noncoding01.fasta").read())
		# remote exon 1
remote_exon01_out = open("remote_exon01.fasta", "w")
remote_exon01_out.write(">AJ223353_exon01_length" + str(len(remote_exon01)) + "\n")
remote_exon01_out.write(remote_exon01)
remote_exon01_out.close()
print(open("remote_exon01.fasta").read())
		# remove noncoding 2
remote_noncoding02_out = open("remote_noncoding02.fasta", "w")
remote_noncoding02_out.write(">AJ223353_noncoding02_length" + str(len(remote_noncoding02)) + "\n")
remote_noncoding02_out.write(remote_noncoding02)
remote_noncoding02_out.close()
print(open("remote_noncoding02.fasta").read())


# open and read local file, convert to upper case
local_seq = open("plain_genomic_seq.txt").read().upper()
	# convert to single line
local_seq_singleline = local_seq.replace("\n","")
	# remove non-DNA chars
local_seq_singleline_anythingleft = local_seq_singleline.replace("G","").replace("A","").replace("T","").replace("C","")i
local_seq_singleline_reallyDNA = local_seq_singleline.replace("X","").replace("S","").replace("K","").replace("L","")
local_seq_singleline_ready = local_seq_singleline_reallyDNA # prep copy for other analyses
	# coding-noncoding, first exon(start to 63rd base), second exon(91st to end)
local_exon01 = local_seq_singleline_ready[0:63]
local_intron01 = local_seq_singleline_ready[63:90]
local_exon02 = local_seq_singleline_ready[90:]
	# write out the files, sequentially
		# local exon 1
local_exon01_out = open("local_exon01.fasta", "w")
local_exon01_out.write(">LocalSeq_exon01_length" + str(len(local_exon01)) + "\n")
local_exon01_out.write(local_exon01)
local_exon01_out.close()
print(open("local_exon01.fasta").read())
		# local intron 1
local_intron01_out = open("local_intron01.fasta", "w")
local_intron01_out.write(">LocalSeq_intron01_length" + str(len(local_intron01)) + "\n")
local_intron01_out.write(local_intron01)
local_intron01_out.close()
print(open("local_intron01.fasta").read())
		# local exon 2
local_exon02_out = open("local_exon02.fasta", "w")
local_exon02_out.write(">LocalSeq_exon02_length" + str(len(local_exon02)) + "\n")
local_exon02_out.write(local_exon02)
local_exon02_out.close()
print(open("local_exon02.fasta").read())

# combined FASTA files
	# coding regions
exons_out = open("All_exons.fasta", "w")
exons_out.write(">AJ223353_exon01_length" + str(len(remote_exon01)) + "\n" + remote_exon01 + "\n")
exons_out.write(">LocalSeq_exon01_length" + str(len(local_exon01)) + "\n" + local_exon01 + "\n")
exons_out.write(">LocalSeq_exon02_length" + str(len(local_exon02)) + "\n" + local_exon02)
exons_out.close()
print(open("All_exons.fasta").read())
	# non-coding regions
introns_out = open("All_noncodings.fasta", "w")
introns_out.write(">AJ223353_noncoding01_length" + str(len(remote_noncoding01)) + "\n" + remote_noncoding01 + "\n")
introns_out.write(">AJ223353_noncoding02_length" + str(len(remote_noncoding02)) + "\n" + remote_noncoding02 + "\n")
introns_out.write(">LocalSeq_intron01_length" + str(len(local_intron01)) + "\n" + local_intron01)
introns_out.close()
print(open("All_noncodings.fasta").read())

exit()

