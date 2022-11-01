pip3 install --user --upgrade pip
pip3 install --user snakemake

# Get BBmap
wget -qO BBMap.tgz 'https://sourceforge.net/projects/bbmap/files/latest/download/'

# GEt velvet
git clone git://github.com/dzerbino/velvet.git velvetSoftware
cd velvetSoftware
make 'OPENMP=1'

# OTher setup
# specifying where 'PATH' is helps the program to use 'PATH' to find where the program is installed
PWD=$(pwd)
PATH=$PATH:/localdisk/home/$USER/.local/bin:$PWD/bbmap:$PWD/velvetSoftware/
OMP_THREAD_LIMIT=24
OMP_NUM_THREADS=24




# check where all the programs are
ls /localdisk/home/$USER/.local/bin

# number of processors > nproc

# help
snakemake -h

# it will search for file called Snakefile

# making a snakemake output from a snakefile
snakemake -s <snakefile> <targets>

# -pn displays shell commands and do a dry run
snakemake -pn <output> -s <snakefile>

Logic is based on
file name patterns
{wildcard} placeholders
snakemake starts with a target filename and looks for rules with a matching output
repeats until it runs out of rules
order of rules in the snakefile is NOT IMPORTANT!

kmersizes are always odd numbers

N50 value


snakemake -pn ds1_plot.pdf -s Snakefile1

snakemake -pn ds1_plot.pdf ds2_filtered_plot.pdf ds1_filtered_plot.pdf -s Snakefile1

snakemake -p --cores 10 ds1_plot.pdf ds2_filtered_plot.pdf ds1_filtered_plot.pdf -s Snakefile1

# rules always communicate via files.