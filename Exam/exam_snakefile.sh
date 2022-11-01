rule plot:
##	output:	'{dataset}_plot.pdf'
##	input: '{dataset}.csv'
##	shell:	'./myplotter.py -o {output} {input}'
	output:
		plot = '{dataset}_plot.pdf'
	input:
		csv = '{dataset}.csv'
	shell:
		'myplotter.py -o {output.plot} {input.csv}'

rule filter:
##	output:	'{csvdata}_filtered.csv'
##	input: '{csvdata}.csv'
##	shell:	'egrep -v ^boring {input} > {output}'
	output:
		csv = '{csvdata}_filtered.csv'
		# insert another distinct output here
	input:
		csv = '{csvdata}.csv'
		# insert another distinct input here
	shell:
		'egrep -v ^boring {input.csv} > {output.csv}'
	"""
	shell:
		r'make_index {input}
			/path/to/my/bin/long_command.py \
			--input_file={input}.idx \
			--consensus_out={output}.consensus_out
		'
	"""
# Making lists 1
ranks = ['kingdom', 'phylum', 'genus']
modi = ['super', 'sub', '']
# expand generates combinations of the pattern in a list, first arg is the template
expand('{m}{r}_list.txt', r=ranks, m=modi)

# Making lists 2
glob.glob('*.csv') # gets all .csv files
cmd = r"ls *.csv | sed 's/.csv/.pdf/'" 
list(shell(cmd, iterable=True)) # makes a list of csv file names into pdf suffix

# curlies in the shell:
{input}
{output}
{wildcards.dataset} # value of 'dataset' wildcard
{adapter} # adapter variable defined at top of snakefile
shell: # double up the curlies
	"awk '{{print $1}}' {input} > {output}"


# Using snakefile on all the files in the folder
# PLot all {data}/*.csv files in one combined plot
# Lambda defers calculating the list
# The snakefile 'foosnake'
rule plot:
	output:
		'{data}_plot.pdf'
	input:
		lambda x: shell("ls {x.data}/*.csv", iterable=True)
	shell:
		"./myplotter.py -o {output} {input}"
snakemake --cores 10 dfiles_plot.pdf -s foosnake
evince dfiles_plot.pdf &

# Another example with a named function, MyDir1 has the files we want to process
ls MyDir1/
# Snakefile called 'foosnake2'
def plot_input(x):
	return shell("ls {x.data}/*.csv", iterable=True)

rule plot:
	output:
		"{data}_plot.pdf"
	input:
		plot_input
	shell:
		"./myplotter.py -o {output} {input}"
snakemake --cores 10 MyDir1_plot.pdf -s foosnake2
ls -alrt
evince MyDir1_plot.pdf &


# Quote elements that have whitespace using `:q`
shell:
	"wc {input:q} > {output:q}"
	# instead of "wc '{input}' > '{output}'"

# Run python code using run: instead of shell:
shell:
	"""for i in {input}; do
			sort -u $i >> {output}
		done
	"""
run:
	# open the output file to write
	with open(output[0], 'w') as ofh:
		for i in input:
			# for each input file, write the unique contents
			# of the input file into the output file
			with open(i) as ifh:
				ofh.write(sorted(set(ifh)))