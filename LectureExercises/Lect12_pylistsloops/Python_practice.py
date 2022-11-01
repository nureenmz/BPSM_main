#!/usr/local/bin/python3

## QUESTION 1
seq1= "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
seq1_countA= seq1.count("A")
seq1_countT= seq1.count("T")
seq1_AT= (seq1_countA + seq1_countT)/len(seq1)

# QUESTION 2
## COMPLEMENTING DNA
seq1low= seq1.lower()
seq1comp= seq1low.replace("a","T")
seq1comp= seq1comp.replace("c","G")
seq1comp= seq1comp.replace("t","A")
seq1comp= seq1comp.replace("g","C")
print("Exons joined\t",seq1comp)

# QUESTION 3
seq2= "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
ecori_motif= "GAATTC"
motif_location= seq2.find(ecori_motif)
motif_count= seq2.count(ecori_motif)
seq2a= seq2[0:22]
seq2b= seq2[22:]
print("Digested fragments\t", seq2a, "and", seq2b) 
seq2b_length= len(seq2b)

# QUESTION 4
seq3= "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
seq3_exon1= seq3[:63] # start to 63rd real char
seq3_exon2= seq3[90:] # 91st real char to end
seq3_ex1ex2= seq3_exon1 + seq3_exon2
seq3_percentseq= (len(seq3_ex1ex2)/len(seq3))*100
print("Coding percentage\t", int(seq3_percentseq))
seq3_intron= seq3[63:90]
seq3_annotated= seq3_exon1 + seq3_intron.lower() + seq3_exon2
print("Sequence 3 EX-int-EX\t",seq3_annotated)



