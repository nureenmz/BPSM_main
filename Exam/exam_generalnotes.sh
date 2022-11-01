grep "motif1" file1
grep "^motif1" file1
grep "motif1$" file1
grep -w "motif1" file1
grep -v "motif1" file1
grep "motif1" file*
grep -c "motif1" file1
grep -m3 "motif1" file1
grep -E "motif1|motif2" file1
egrep "motif1|motif2" file1
grep -Ei "motif1|motif2" file1

### awk ###
"""
$1 first field
$0 whole line
$NF Last field
FS ' '
() evaluation command
{} action command
"""
awk '($3==5)' file1
	# output ROWS where third field has a 5
awk '{FS="\t"; if($3==5){print $0;}}' file1
awk '{FS="\t"; if($3 == "foobar1"){print $0;}}' file1
awk '{FS="\t"; OFS="_"; if($3 == "foobar1"){print $1,$2,$3;}}' file1
awk '{FS="_"; print NF;}' file1 # output the number of fields on the line
awk '{FS=" "; print "There are",NF,"fields on this line.";}' file1
awk '{FS="XXX"; print "The last field on this line is",$NF ;}' file1 # output the actual last field on the line
awk '{FS="\t"; if($3 == "United Kingdom"){print $0;}}' file1 > file2 # pipe the wholeline into file2
awk '{FS=" "; if($3 == "United Kingdom"){print $0;}}' file1 > file2 # changed the FS this time.. differnt output from above!

# if first three chars of third field of file1 are 'Uni', 
	# then append first field to file2
awk 'BEGIN{FS="\t";}
{
	if(substr($3,1,3) == "Uni")
		{print $1;}
}' file1 >> file2

awk '{if($6==1991){print $1}}'



