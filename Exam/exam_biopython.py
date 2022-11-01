#!/local/bin/python3

import subprocess, os, re
import numpy as np
from Bio import SeqIO
from Bio import Entrez

while True:
	try:
		os.mkdir('GENCODE')
		os.chdir('GENCODE')
		break
	except FileExistsError:
		os.rmdir('GENCODE')
		continue

gencodefile = 'gencode.v38.pc_transcripts.fa.gz'
cmd = fr'wget -qnv https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_38/{gencodefile}'
subprocess.call(cmd, shell=True)
subprocess.call(fr'gunzip {gencodefile}', shell=True)

# this is a FastaIterator, not the sequence itself!
sequences = SeqIO.parse(gencodefile.replace('.gz',''), 'fasta')
count = 0
allCDS = []
allcodingseqs = []
for record in sequences:
	example = record
	#print('Dummy text')
	#print(f'example.id shows the associated ID {example.id}')
	#print(f'example.seq shows the sequence record {example.seq}')
	#CDS.translate() # translates the sequence's coding region
	CDSindex = re.findall(r'(?<=CDS:)(\d+)-(\d+)(?=|)', example.id)[0]
	allCDS.append(CDSindex)
	start = int(CDSindex[0])-1
	end = int(CDSindex[1])
	codingseq = example.seq[start:end]
	allcodingseqs.append(codingseq)
	count += 1
#start, startcounts = np.unique(startcodon, return_counts=True)
#stop, stopcounts = np.unique(stopcodon, return_counts=True)
#print(f'{count} sequences processed')
#print(allCDS)
#CDSindex = [i.split(':')[1].split('-') for i in example.id.split('|') if i.startswith('CDS')][0]
#CDSindex = [re.findall(r'\d+', i) for i in example.id.split('|') if i.startswith('CDS:')][0]

# Number of k-mers
# THe number of Non-overlapping kmers: N_k = L // k
# The number of overlapping kmers: N_k = L-k+1
"""K-mer counting: non-overlapping
"""
k=3
for i in range(0,len(DNA)-k+1,k):
	print(i, DNA[i:i+k])
"""K-mer counting: overlapping
"""
# last index to consider
for i in range(0,len(DNA)-k+1):
	print(i, DNA[i:i+k])

from Bio.Seq import Seq
sequence  = Seq(someDNAstring).upper()
sequence.translate(to_stop=True)
sequence.reverse_complement().translate(table=3) #default is table 1

sequences_dict = SeqIO.to_dict(SeqIO.parse(gencodefile.replace('.gz',''), 'fasta')) #use SeqIO twice
sequences_dict.keys()
list(sequences_dict.values())[index]

gbfile = "/localdisk/data/BPSM/Lecture19/sequence.gb"
gbseq = SeqIO.parse(gbfile, "genbank")
gbseqrecord = next(gbseq) # saves the record to a variable, no need to re-parse
gbseqrecord.annotations # to see all the key/value pairs
gbseqrecord.annotations['taxonomy']
gbseq_seq = gbseqrecord.seq[0:] # can be indexed
Seq(gbseqrecord.seq[0:].translate(table=1)) # frame 1
Seq(gbseqrecord.seq[1:].translate(table=1)) # frame 2
Seq(gbseqrecord.seq[2:].translate(table=1)) # frame 3

for feature in gbseqrecord.features:
	if feature.type in {'source','CDS'}:
		print(feature.type, feature.location)

wanted = 'ND2'
for i, feat in enumerate(gbseqrecord.features):
	if feat.qualifiers.get('gene'):
		gene_string = ''.join(str(e) for e in feat.qualifiers.get('gene'))
		if gene_string == wanted:
			print(f'\nfeature number {i+1} containing {wanted}')
			print(feat, feat.qualifiers['gene'])
	else:
		print(f'\nfeature number {i+1} does not contain {wanted}')

ND2feature = gbseqrecord.features[4] # type, location, qualifiers (is a dict)
ND2feature.extract(gbseqrecord).seq.translate() # extract sequence from a feature

"""Viewing format
print(                                      # fifth: print the joined things to screen
 "\n".join(                                 # fourth: join the findall list elements with a new line
  re.findall(r'.{1,30}',                    # third: find 1-30 character stretches in the string
  str(                                      # second: make the translation into a string
     new_ND2_record.seq.translate(table=5)  # first: get and translate the sequence
     )                                      # close str 
            )                               # close findall
          )                                 # close join
     )                                      # close print
"""

"""Using ENTREZ
"""
from Bio import Entrez
Entrez.email = 's2255686@ed.ac.uk'
Entrez.api_key = subprocess.check_output("echo $NCBI_API_KEY", shell=True).rstrip().decode('utf-8')

entrezrecord = Entrez.read(Entrez.einfo()) # get a list of entrez databases
entrezrecord.values()

entrezpubmed = Entrez.read(Entrez.einfo(db='pubmed'))
entrezpubmed['DbInfo'].keys()
entrezpubmed['DbInfo']['DbINfo']
#and so on.. it gets really complicated...

# Entrez to search GenBAnk for seq records (multiples)
mysearch = Entrez.esearch(db="nucleotide", term="COX1", retmax="1000") # define the search
mysearchresult = Entrez.read(mysearch) # do the search
mysearchresult.keys()
COX1_ids = mysearchresult['IdList'][0:5] # get the id list of the first 5 results
# append genbank entry of each ID to a list
COX1_ids_genbank=[]
for id in COX1_ids:
	genbank = Entrez.efetch(db="nucleotide", id=id, rettype="gb", retmode="text")
	record = SeqIO.read(genbank, 'genbank')
	COX1_ids_genbank.append(record) # appends as Genbank format
	print(f'COX1\t{record.description}')

# Another entrez example
mysearch2 = Entrez.read(Entrez.esearch(db='protein', term='COX1 AND txid130642[orgn]', retmax='1000'))
for i,id in enumerate(mysearch2['IdList']):
	genbank = Entrez.efetch(db='protein', id=id, rettype='gb')
	record = SeqIO.read(genbank, 'genbank')
	# SeqIO.write(SeqRecordobject, handle, format)
	with open('cosmocarta_COX1.prot.gb', 'a') as gb:
		SeqIO.write(record, gb, 'genbank')
	print(i+1, record.id, record.description)

search_results=[]
def get_avg_len(email, dbtype, taxonomy, gene, howmany=10):
	"""returns avg seq length of first n results
	keeping the outputs,
	and write search result to a file
	"""
	from Bio import Entrez, SeqIO
	import os, subprocess
	Entrez.email = email
	Entrez.api_key = subprocess.check_output("echo $NCBI_API_KEY", shell=True).rstrip().decode('utf-8')
	# do the search
	search_term = f'{taxonomy} {gene} complete'
	mysearch = Entrez.esearch(db=dbtype, term=search_term, retmax=howmany)
	mysearchresult = Entrez.read(mysearch)
	# write to a file
	filename = f"{search_term.replace(' ','_')}_outputs.txt"
	search_output = open(filename, 'w')
	# get info from search results
	total_len = 0
	for i,accession in enumerate(mysearchresult['IdList']):
		genbank = Entrez.efetch(db=dbtype, id=accession, rettype='gb')
		record = SeqIO.read(genbank, 'genbank')
		total_len = total_len + len(record.seq)
		search_results.append([search_term, record.id, record.description, len(record.seq), record.seq])
		search_output.write(f'{record.id}\t{record.description}\t{str(len(record.seq))}\t{str(record.seq)}\n')
		print(record.id, len(record.seq))
	avg_len = int(total_len/(i+1))
	return print(f'\nThe mean length was {avg_len} amino acids.\n')
	close(search_output)

get_avg_len('s2255686@ed.ac.uk', 'protein', 'arthropoda', 'ATP6')
[print(result) for result in search_results]
