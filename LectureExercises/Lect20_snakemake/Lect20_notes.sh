pip3 install --user --upgrade pip
pip3 install --user snakemake

# check where all the programs are
ls /localdisk/home/$USER/.local/bin

# number of processors > nproc

# help
snakemake -h
snakemake -v

# making a snakemake output from a snakefile
snakemake -s <snakefile> <targets>

# -pn displays shell commands and do a dry run
snakemake -pn <output> -s <snakefile>

"""
It will search for file called Snakefile

Logic is based on:
	- file name patterns
	- curly brackets are {wildcard} placeholders
	- snakemake starts with a target filename and looks for rules with a matching output
	- repeats until it runs out of rules
	- order of rules in the snakefile is NOT IMPORTANT!

Rules always communicate via files

Kmersizes are always odd numbers

N50 value is a statistic that:
	1. Describes the distribution of contig lengths
	2. Estimate completeness of the assembly

"""

snakemake -pn ds1_plot.pdf -s Snakefile1

snakemake -pn ds1_plot.pdf ds2_filtered_plot.pdf ds1_filtered_plot.pdf -s Snakefile1

snakemake -p --cores 10 ds1_plot.pdf ds2_filtered_plot.pdf ds1_filtered_plot.pdf -s Snakefile1

# for workflow that has the file name specified, run snakemake directly
	# dry run
snakemake -pn --cores 1 -s SnakefileEx
	# actual run
snakemake -p --cores 10 -s SnakefileEx
ls -altrR snakeout

# for workflow that has a wildcard file input, insert output file name
snakemake --cores 10 -p <someoutputfilename> -s <somesnakefile>



# Get velvet
git clone git://github.com/dzerbino/velvet.git velvetSoftware
cd velvetSoftware
# Compile the source code. 'Makefile' tells the compiler what to do.
make 'OPENMP=1'
ls -ls
cd ..
# Other setup
# specifying where 'PATH' is helps the program to use 'PATH' to find where the program is installed
PWD=$(pwd)
PATH=$PATH:/localdisk/home/$USER/.local/bin:$PWD/velvetSoftware/:$PWD/bbmap
OMP_THREAD_LIMIT=24
OMP_NUM_THREADS=24
velveth -h # for help on velvet
"""Velvet is run in two steps
1. velveth produces a hash table for velvetg to use
2. velvetg builds and manipulate the De Bruijn graph and produces the assembly
"""

# Get BBmap
wget -qO BBMap.tgz 'https://sourceforge.net/projects/bbmap/files/latest/download/'
tar xvfz BBMap.tgz
ls BBMap


"""Velvet assembly: MANUAL
"""
cp /localdisk/data/BPSM/Lecture20/6991* .
fq1='6991_1.fastq.gz'
fq2='6991_2.fastq.gz'
velveth paired_k21 21 -shortPaired -fastq.gz -separate $fq1 $fq2
velvetg paired_k21
# obtain information about the assembly using stats.sh
# first run setup to get bbmap
stats.sh paired_k21/contigs.fa # save this output to a file?


"""Velvet assembly: SNAKEMAKE
"""
# run velveth and velvetg in one shell job
# use r""" to enclose multiple shell commands
# use {sample} wildcard in filenames of all input and output
# give names to the multiple inputs
# reference named inputs using curlies and dot i.e. {input.read1}
# mv is used to rename the output file (not customizable in velvetg)
# ignore various other files that velvet produces

# foosnake3
rule assemble:
	output: "{sample}_paired_k21_contigs.fa"
	input:
		read1 = "/localdisk/data/BPSM/Lecture20/{sample}_1.fastq.gz",
		read2 = "/localdisk/data/BPSM/Lecture20/{sample}_2.fastq.gz"
	shell:
		r"""velveth paired_k21 21 -shortPaired -fastq -separate {input.read1} {input.read2}
		velvetg paired_k21
		mv paired_k21/contigs.fa {output}
		"""
rule stats:
	output: 
		full = "{assembly}_contigs_stats.txt",
		grepped = "{assembly}_contigs_stats_grepped.txt"
	input: "{assembly}_contigs.fa"
	shell:
		r"""stats.sh {input} > {output.full}
		stats.sh {input} | grep contig > {output.grepped}
		"""

snakemake -p --cores 10 6991_paired_k21_contigs_stats.txt -s foosnake3

# Try a range of kmer values
# Summarise the N50 stats at the end
# by expanding lists to be wildcards
# redirect outputs to a separate folder velvetOUT and snakeout
# foosnake4
samples = ['6991']
kmers = range(19,32,2)

rule assemble:
	output: 
		"snakeout/{sample}_paired_k{kmer}_contigs.fa"
	input:
		read1 = "/localdisk/data/BPSM/Lecture20/{sample}_1.fastq.gz",
		read2 = "/localdisk/data/BPSM/Lecture20/{sample}_2.fastq.gz"
	shell:
		r"""velveth velvetOUT {wildcards.kmer} -shortPaired -fastq -separate {input.read1} {input.read2}
		velvetg velvetOUT
		mv velvetOUT/contigs.fa {output}"""

rule stats:
	output:
		full = "snakeout/{assembly}_contigs_stats.txt",
		grepped = "snakeout/{assembly}_contigs_stats_grepped.txt"
	input:
		"snakeout/{assembly}_contigs.fa"
	shell:
		"""stats.sh {input} > {output.full}
		stats.sh {input} | grep contig > {output.grepped}"""

rule all_kmer_stats:
	output:
		"snakeout/all_stats.txt"
	input:
		expand('snakeout/{s}_paired_k{k}_contigs_stats.txt', s=samples, k=kmers)
	shell:
		"grep -H 'contig N/L50' {input} > {output}"

snakemake -p --cores 10 -s foosnake4
