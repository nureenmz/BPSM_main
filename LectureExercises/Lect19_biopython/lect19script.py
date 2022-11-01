import os, sys, subprocess,shuti, glob
import pandas as pandas
import numpy as np

import Bio

"""
Seq specifies a sequence
myseq= Seq('string').upper()

myseq.translate(to_stop=True) # translate until it reaches a stop codon

myseq.reverse_complement().translate()

myseq.translate(table=1) # table here is the codon usage table

---

fastapath= '/localdisk/data/BPSM/Lecture19/sequences.fasta'

records= SeqIO.parse(fastapath, 'fasta') # opens the fasta file, with format

for seqrecord in records:
	print(seqrecord.id)
	print('\t'+seqrecords.seq.translate()) # translates the seq and prints

next(records) # shows the first record, second time shows second record

# do the parsing again to 're-read' the record as a fresh variable

fastadict= SeqIO.to_dict(SeqIO.parse(fastapath, 'fasta')) # make parse into a dictionary

list(fastadict.keys()) # get the keys

fastadict.values()

len(fastadict.items())

print(list(fastadict.values())[0])

----

mito= next(SeqIO.parse('sequence.gb', "genbank"))

mito.annotations # a dictionary

mito_seq= str(mito.seq) # get just the sequence
OR 
Seq(mito_seq[1:]) # substring the sequence [0:], [1:], [2:] to all three reading frames
Seq(mito_seq[1:]).translate(table=1) # translate

----

# get seq features from genbank format
records = SeqIO.parse(my_gbfile, "genbank")
for seq_record in records: # gets the first record
    for feature in seq_record.features: # gets the features
        print(feature.type) # print the key 'CDS'
        print(feature.location) # print the location of 'CDS' on the sequence

tRNA 58...112		# features
/product='tRNA-Ser'	# qualifiers

# get features again
records = SeqIO.parse(my_gbfile, "genbank") # this dies after one use

to use it again and again:
list(SeqIO.parse(my_gbfile, "genbank"))
MyGenbank_record = next(SeqIO.parse(my_gbfile, "genbank") # save the record
MyGenbank_record. tabtab

----

# searching for a gene 'ND2' in the Features
wanted="ND2"
counter=0
for each_feat in MyGenbank_record.features :
   counter += 1
   if each_feat.qualifiers.get('gene') :
        genename_string="".join(str(e) for e in each_feat.qualifiers.get("gene"))
        if genename_string == wanted :
          print("\n### ",counter,wanted,"\n",each_feat,each_feat.qualifiers['gene'])

myND2feature = MyGenbank_record.features[4]
my_ND2_feature.type 	# 'CDS'
my_ND2_feature.qualifiers


"""
Entrez.api_key= api_key=subprocess.check_output("echo $NCBI_API_KEY", shell=True).rstrip().decode('utf-8')
Entrez.email = 's2255686@ed.ac.uk'
records= Entrez.read(Entrez.einfo())
records_pubmed= Entrez.read(Entrez.einfo(db='pubmed'))

# How many complete COX1 protein records are there for mammals?
mysearch= Entrez.esearch(db='protein', term= 'COX1[protein] AND mammalia[Organism] complete')
result= Entrez.read(mysearch)
counter= 1
for accession in result['IdList']:
	genbank= Entrez.efetch(db='protein', id= accession, rettype= 'gb')
	records= SeqIO.read(genbank, 'genbank')
	print(counter, 'COX1', records.description) # only prints up to 20??
	counter += 1
print('There were {} records found'.format(str(result['Count'])))


# What is their average length (the proteins that is, not the mammals!)?


Write a function that will answer the question for any gene name and any taxonomic group.

def get_average_length(taxonomy, gene, startat=0,howmany=100):
    from Bio import Entrez, SeqIO
    Entrez.email = "s123456@ed.ac.uk"
    Entrez.api_key=subprocess.check_output("echo $NCBI_API_KEY", shell=True).rstrip().decode()
    search_term = taxonomy + " " + gene + " complete"
    search_output = open(search_term.replace(" ","_")+"_outputs.txt","w")
    mysearch = Entrez.esearch(db="protein", term=search_term, retstart = startat, retmax=howmany)
    result = Entrez.read(mysearch)
    print("Search done,", result['Count'],"found, starting retrieval of",howmany,"starting at",startat)
    loopcounter = poorseqs = total_length = 0
    for accession in result['IdList']:
      loopcounter += 1
      genbank = Entrez.efetch(db="protein",id=accession,rettype="gb")
      print('\r' + 'Retrieving sequence ' + str(loopcounter+startat), end="")
      record = SeqIO.read(genbank, "genbank")
      Xaa = str(record.seq).count("X")
      if Xaa > 5 :
         print(" Seq",loopcounter+startat,"contains",Xaa,"unknown amino acids:",int(100*Xaa/len(record.seq)), "percent of total!")
         poorseqs += 1
      else :
         total_length =  total_length + len(record.seq)
         search_results.append([search_term,record.id,record.description,len(record.seq),record.seq])
         # print(record.id+"\t"+record.description+"\t"+str(len(record.seq))+"\t"+record.seq[0:50]+"...")
         search_output.write(record.id+"\t"+record.description+"\t"+str(len(record.seq))+"\t"+str(record.seq)+"\n")
    goodseqs=loopcounter-poorseqs
    mean_length = int(total_length/goodseqs)
    return print(("\nThe mean length of the "+str(goodseqs)+" high quality seqs was "+str(mean_length)+" amino acids.\n"))
    close(search_output)

get_average_length2('Bos taurus', 'cytochrome c oxidase subunit I (mitochondrion)',1,1000)


# bulk download of sequences
search_term="Mammalia COX1"
mysearch = Entrez.esearch(db="protein", term=search_term, retmax=100000)
result = Entrez.read(mysearch)
...
...


