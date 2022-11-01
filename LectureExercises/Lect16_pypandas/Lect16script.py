## INTRO TO PANDAS ##

	# for dealing with tabular data (excel, etc)
	# https://pandas.pydata.org/

python3
import os, sys, subprocess
import numpy as np
import pandas as pd
	## pandas not in bioinfmsc7: subprocess.call("pip3 install pandas",shell=True)
	# pip3 = install for python3, dependencies = stuff pandas need to fxn

	# 'SERIES' - like a list, but has an index, its elements have a type
s1= pd.Series(['a','b','c','d'])
s2= pd.Series([2,4,8,16])
pd.Dataframe( { 'letter' : s1, 'number' : s2 } ) # note the curly brackets

	# file from NCBI containing eukaryotic genome seqs
subprocess.call('wget -qO eukaryotes.txt "ftp://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/eukaryotes.txt" ' , shell=True) # 0 is exit code = no mistakes
os.system("head -3 eukaryotes.txt")

	# import the file as a dataframe table
	# first line= header row, karg= separator, df= dataframe variable name, explicit index from zero
	## help(pd.read_csv)
	#read the file in
df= pd.read_csv('eukaryotes.txt', sep="\t", na_values=['-']) # na_values: missing data is in hyphen
df.shape # get df size
df.columns # get column headings, spacing not an issue bcs sep="\t"
	## list(df.columns)
	## df[3:7] #slices - rows 3 to 6 according to the index, including colhead
df.head()
df.describe # tries to summarize stuff with numbers in the df, will not calc if there r missing vals
df['#Organism/Name'] #extract col by colhead name, must be exact
df['#Organism/Name'].value_counts() # count unique vals in a series, auto sorted, returns SERIES
df[ ['#Organism/Name', 'Size (Mb)', 'GC%'] ].head() # can also give list of colnames. returns DATAFRAME

df['#Organism/Name'] == 'Arabidopsis thaliana' # get which row that matches
(df['#Organism/Name'] == 'Arabidopsis thaliana').value_counts() # count how many rows that says true/false
	#OR use <isin>
df[df['#Organism/Name'].isin(["Arabidopsis thaliana"])].shape 

	# make subset of the data, writes it to csv file (tab sep)
cress = df[df['#Organism/Name'] == 'Arabidopsis thaliana']
cress.to_csv("All_the_Arabidopsis_ones.tsv", sep="\t", header=True)
	# filter/extract stuff
	# sizes of all the genomes
sizes= df[df['#Organism/Name'] == 'Arabidopsis thaliana']['Size (Mb)']
sizes.describe()
	# OR other ways
df[df['Size (Mb)'] > 10000] # see sizes bigger than 10000Mb
	# & to join multiple queries
df[ (df['Size (Mb)'] > 10000) & (df['Status'] == 'Scaffold') ]

	# apply(): runs arbitrar expressions on rows
	# axis=1 iterate over rows
	# make all org names upper case
df.apply(lambda x : x['#Organism/Name'].upper(), axis=1).head()
	# look for something
'Birds' n set(df['SubGroup'])
	# find birds and mammals with small genomes
df[df.apply( lambda x : x['Size (Mb)'] < 500 and x['SubGroup'] in ['Birds'], axis=1 )]
df[df.apply( lambda x : x['Size (Mb)'] < 500 and x['SubGroup'] in ['Mammals'], axis=1 )]
	# joining both queries, birds 'or' mammals
birds_n_mammals=df[df.apply( lambda x : x['Size (Mb)'] < 500 and x['SubGroup'] in ['Birds', 'Mammals'], axis=1 )]

	# sort_values()
	# get the largest genomes
df.sort_values('Size (Mb)', ascending=False).head() # add <inplace=True> to override original df
df['Size (Mb)'] # now this is sorted by size
	# sort on by name ascending, and GC descending
df.sort_values(['#Organism/Name', 'GC%'], ascending=[True,False]).head()

	# creating a column AT content
df['at_content']= 1-(df[GC%']/100)
df[ ['#Organism/Name', 'GC%', 'at_content'] ].head() #check the new column
	# cannot 'split', but can use apply to extract
df['genus']= df.apply(lamda x: x['#Organism/Name'].split(' ')[0], axis=1)
df[ ['#Organism/Name', 'genus'] ].head() # view the columns, note the sq brackets

	# descriptive statistics
print(df[ ['Size (Mb)', 'GC%'] ].mean())
	#etc..

	# indexing
	# specify something as index instead of the explicit number index at FIRST READ
df2= pd.read_csv('eukaryotes.txt', sep="\t", na_values=['-'], index_col='Assembly Accession')
df3= pd.read_csv('eukaryotes.txt', sep="\t", na_values=['-'], index_col='#Organism/Name')
	# specify index after done initial read
df3.set_index('BioSample Accession')
	# customize an index by org name and acc number
df = pd.read_csv('eukaryotes.txt', sep="\t", na_values=['-'])
df.index= df.apply(lambda x : "{} ({})".format(x['#Organism/Name'], x['BioSample Accession']), axis=1) # this doesn't remove the indexed columns from total column count
	# INDEX BY SOMETHING USEFUL FOR EASIER VIEW
df.index.value_counts()
df['TaxID'].values[0:3]

	# selections using <iloc>
	# get single rows, in key/value format
df.iloc[0]
df.iloc[-1]
	# single columns
df.iloc[:,0]
df.iloc[:,-1]
df.iloc[0:5]                 # first five rows of dataframe
df.iloc[:, 0:2]              # first two columns of data frame with all rows
df.iloc[ [0,3,6,24], [0,5,6] ] # 1st, 4th, 7th, 25th row + 1st 6th 7th columns.
df.iloc[0:5, 5:8]            # first 5 rows and 5th 6th 7th columns
df.columns[5:8], df.iloc[0:5, 5:8]
	# <loc> indexer: use lke iloc, 
data.loc[<rows>,<cols>]
df.loc['Glycine max (SAMN00002965)'] # select by label
df.loc[ ['Glycine max (SAMN00002965)','Solanum lycopersicum (SAMN02981290)'] ]

df.loc[ ['Glycine max (SAMN00002965)','Solanum lycopersicum (SAMN02981290)'],['TaxID','Size (Mb)','GC%','Genes'] ]
df.loc[ ['Glycine max (SAMN00002965)','Solanum lycopersicum (SAMN02981290)'],list(df.columns[ [1,6,7,12] ])]

	# Count number of genes
df['Genes'].value_counts()
df[['#Organism/Name','Genes']].value_counts()
	# Aggregate
df['Genes'].agg('min')
df['Genes'].agg('max')
df['Genes'].agg(['max','min','mean','std'])
	# Groupby (get all rows with that criteria and get mean of the numbers)
df.groupby('#Organism/Name').mean()
df.groupby('#Organism/Name').mean().iloc[:,0:3] # can also subset that

Index(['#Organism/Name', 'TaxID', 'BioProject Accession', 'BioProject ID',
       'Group', 'SubGroup', 'Size (Mb)', 'GC%', 'Assembly Accession',
       'Replicons', 'WGS', 'Scaffolds', 'Genes', 'Proteins', 'Release Date',
       'Modify Date', 'Status', 'Center', 'BioSample Accession'],
      dtype='object')


#-------EXERCISES
df=pd.read_csv('eukaryotes.tsv', sep="\t", na_values=['-'])
df.index=
# how many fungal species have genomes bigger than 100Mb? What are their names?
df.columns
set(df['Group'])
fungal_genomegt100= df[df.apply( lambda x : x['Size (Mb)'] > 100 and x['Group'] == 'Fungi', axis=1 )]
len()
fungal_genomegt100['#Organism/Name'].value_counts() # Length: 95
orgname_fungal_genomegt100= (set(fungal_genomegt100.iloc[:,0]))

big_fungi= df[(df['Group'] == 'Fungi')&(df['Size (Mb)']>100)]
list(big_fungi['#Organism/Name'])

# how many of each Kingdom/group (plants, animals, fungi and protists) have been sequenced?
df['Group'].value_counts()

# which Heliconius species genomes have been sequenced?
hel= df[df.apply(lambda x: x['#Organism/Name'].startswith('Heliconius'), axis=1)]
hel[ ['#Organism/Name', 'Scaffolds'] ]


# which sequencing centre has sequenced the most plant genomes? the most insect genomes?
seq_center_plants= df[df['Group'] == 'Plants']['Center'].value_counts().head()
seq_center_insects= df[df['SubGroup'] == 'Insects']['Center'].value_counts().head()

# add a column giving the number of proteins per gene. Which genomes have at least 10% more proteins than genes?
df['Proteins per gene']= df['Proteins']/df['Genes']
df[ ['#Organism/Name', 'Group', 'Proteins per gene'] ].head()

out= df[df['Proteins per gene']>=1.1][['#Organism/Name', 'Genes', 'Proteins', 'Proteins per gene']].head()
len(out)

