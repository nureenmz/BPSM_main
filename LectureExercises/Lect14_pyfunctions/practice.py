def get_at_content(some_dna):
	length= len(some_dna)
	a_count= some_dna.upper().count('A')
	t_count= some_dna.upper().count('T')
	at_content= (a_count + t_count)/length
	return at_content

my_dna= 'adtgctagctgatsgct'

at= get_at_content(my_dna) #store returned output in a variable

	# internal variables only exist in the fxn (hence "internal")
	# no "return" line means no result
	# once it process the return line, it will come out of the fxn ie. break

# calc AT cont of a file
dna2= open('dna2.txt').read()
at= get_at_content(dna2)
#OR
at= get_at_content(open('dna2.txt').read()

# write AT content of a seq to a file
result= open('output.txt', 'w')
result.write(str(get_at_content('ACTTcGa')))
result.close
#OR
with open('output.txt', 'w') as result:
	result.write(str(get_at_content(fkdsjdhsf)))
	#check
result.closed
print(open("output.txt").read())


# encapsulation breaker 1
	# don't use a value that exist outside fxn as part of fxn
	# None (datatype) = null value, (not 0 / false/ empty string)
# encapsulation breaker 2
	# don't write a fxn that only PRINTS value i/o returning it
	# when assigned to variable (fxn that PRINTS), you won't get back the actual fxn output

# input > "arguments"; output > "return"

# VER 2
def get_at_content(some_dna):
        length= len(some_dna)
        a_count= some_dna.upper().count('A')
        t_count= some_dna.upper().count('T')
        at_content= (a_count + t_count)/length
        return round(at_content, 2) # two decimal places of the output
# VER 3
def get_at_content_v3(some_dna, sig_figs):
        length= len(some_dna)
        a_count= some_dna.upper().count('A')
        t_count= some_dna.upper().count('T')
        at_content= (a_count + t_count)/length
        return round(at_content, sig_figs) # more flexible to specify how many s.f to output
# VER 4
def get_at_content_v4(some_dna, sig_figs=2):
        length= len(some_dna)
        a_count= some_dna.upper().count('A')
        t_count= some_dna.upper().count('T')
        at_content= (a_count + t_count)/length
        return round(at_content, sig_figs) # set default at 2, but can change it when specified


## Keyword arguments
get_at_content_v4(some_dna= blablabla, sig_figs=2) # when specified, order doesn't matter

# To check fxn works - print!
for base in 'gatcx':
	print("Was A or T? "+ base.upper() + ": "+str(get_at_content_v4(base) == 1)

# assert - test fxn for which we know answer
assert get_at_content_v4("A") == 1 # if true, no output
assert get_at_content_v4("AAA") ==3 # if false, we get assertion error
# assertion is problematic with floats
	# use "round"
assert round(functionhere(arguments), 2) == output_value
# OR "round" in the fxn first
def functionhere(arguments):
	return round(output_value)



## EXERCISES

def percentage_aa_prot(prot_seq, amino_ac):
	aa_count= prot_seq.count(amino_ac)
	return (aa_count/len(prot_seq)*100)

def percentage_aa_prot_v2(prot_seq, amino_ac=['A','I','L','M','F','W','Y','V']):
        count= 0
	for letter in amino_ac:
		aa_count= prot_seq.count(letter)
        	count= count+(aa_count/len(prot_seq)*100)
	return count

def undetermined_bases(dna_seq, threshold):
        count= 0
        for bases in dna_seq.upper():
		if 'A' not in bases and 'T' not in bases and 'C' not in bases and 'G' not in bases:
                	count += 1
	percent= (count/len(dna_seq))*100
        return percent >= threshold

def kmers_threshold(dna_seq, ksize=2, kmin=3): 
	#---error trap
	if ksize > len(dna_seq):
		return "kmer length longer than DNA"
	if ksize < 2 or ksize > 50:
		return "Inappropriate kmer length. Input length between 3 to 49 only"
	#---end of error trap
	print("Processing DNA seq of length", len(dna_seq), "kmer size", ksize, "and frequency at least", kmin)
	kfound= []		
	kmerrange= list(range(0,len(dna_seq)))
	# then get the kmer sequences
	for firstbase in kmerrange:
		if (firstbase+ksize) < len(dna_seq)+1:
			seqout= (dna_seq)[firstbase:firstbase+ksize]				
			kfound= kfound + [seqout]
 			# get freqs of non-redundant set
	uniqueset= list(set(kfound))
	out= []
	for freqs in uniqueset:
		if kfound.count(freqs) >= kmin:
			out.append(freqs.upper()+": "+str(kfound.count(freqs)))
	return out

# error trap for inserting DNA only
# error trap for integer only
# error trap for empty
# error trap for returning to reinput value

# can you open a file, then use its contents as input to a function??

# save the function as a file, then call it in another script
import name_of_a_function # file name is name_of_a_function.py


