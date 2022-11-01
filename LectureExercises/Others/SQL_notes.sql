### SQL lecture notes ###

psql --help

-h PostgreSQL server IP address
-d database name
-U user name
-p port which PostgreSQL server is listening on
-f path to SQL script
-a all echo
-q quiet

# call script within pSQL
\i script.sql
# call script within bash - passed to psql
psql -U bpsm2017 -d s2255686 -a -f script.sql
# same as above but provide password
echo $PGPASSWORD
export PGPASSWORD = thisismypassword
psql -h localhost -d mydb -U user -p 5432 -a -q -f /localdisk/home/s2255686/script.sql

# login, pw is BPSM2017
psql -U bpsm2017 $user
# get help
\h ;
# create table
create table sample_table (id int, scientific_name text, common_name text, location text) ;
create table sequence_table (id int, seq text, length int, sample_id int) ;
create table hit_table (id int, length int, accession text, score int, sequence_id int) ;
# describe all tables, or a table
\d
\d sample_table
# add row to a table, columns must be in same order
insert into sample_table
values
(1,'Homo sapiens','human','Edinburgh'),
(2, 'Columba livia','pigeon', 'Stirling'),
(3, 'Sciurus vulgaris','red squirrel', 'Aberdeen') ;
# show all rows in a table, * means all columns, top 3 rows,
select * from sample_table ;
select id, common_name from sample_table ;
select * from sample_table limit 3 ;
# filter on individual columns, then order
select length, accession from hit_table where length > 100 order by length asc;
# combine info from two tables
	# tell the db relationship between two tables (sample_id and id are the same)
select seq, length, common_name
	from sequence_table, sample_table
	where sequence_table.sample_id = sample_table.id ;
	
	# seq length + common name + accession number + length>100
select sequence_table.length, sample_table.common_name, hit_table.accession
	from sequence_table, sample_table, hit_table
		where sequence_table.sample_id = sample_table.id
			and
		hit_table.sequence_id = sequence_table.id
			and
		hit_table.length > 100 ;
# remove a row
delete from sample_table where id=1 ;
delete from sample_table where common_name='fox' ;
# empty table contents, preserve headings
truncate sample_table ;
# delete the table
drop table sample_table ;
# updating table contents
UPDATE tablename
SET
	column1 = new_value1,
	column2 = new_value2
WHERE
	id = idvalue ;
# import entire csv table
\copy hit_table
	from '/path/hitfile.csv'
	delimiter ',' csv ;
# import specific columns of csv table
\copy hit_table(id,length,accession,score,sequence_id)
	from '/path/hitfile.csv'
	delimiter ',' csv header ;

# alter table to enforce uniqueness by creating an implicit index
alter table sample_table add primary key (id) ;
	# called sample_table_pkey
	# pkey must contain UNIQUE and non-null values
	# only ONE pkey per table (but can be single or multiple fields)
	# setting the pkey early on helps to not put duplicate entries

# alter table to relate it to another table by creating a foreign key
# a column in sequence table refers to a column in sample table
alter table sequence_table
	add foreign key (sample_id) # child
	references sample_table(id) ; # parent

# alter table so that the column cannot be null ie. a `not-null` contraint
alter table sample_table
	alter column location
	set not null ;

# other considerations
	# think of database design first = flow chart
	# when a table is linked to another, cannot simply drop that table
	# you will then have to cascade drop the other tables too

# sort outputs from SQL queries
select
	hit_table.id, hit_table.length, hit_table.accession, sequence_table.seq
from
	hit_table, sequence_table
where
	hit_table.sequence_id = sequence_table.id
order by
	length desc ;
# make copy of table
create table sequences_next
	as table sequence_table ;
# make subset of table
create table sequences_subset as
select
	seq, length, common_name
from
	sequence_table, sample_table
where
	sequence_table.sample_id = sample_table.id
	and
	common_name = 'human' ;

# count things
# number sequences longer than 100 bases, which ones, show the sequences
select count(*) from sequence_table where length>100 ;
select * from sequence_table where length>100 ;
select seq from sequence_table where length>100 ;
# how many sequences from each sample
select common_name, count(*)
from sequence_table, sample_table
where sequence_table.sample_id = sample_table.id
group by sample_table.common_name
order by count desc ;
# average things `avg()`
# add things `sum()`

# exporting data
\copy hit_table to 'all_hits_table.csv' delimiter ',' csv header ;
\copy hit_table to 'all_hits_table.tsv' delimiter e'\t' ; # no header if tab-delim

\copy (select * from sample_table) to 'mysampletable.csv' (format csv, delimiter ';')
\copy (select * from sample_table) to 'mysampletable.xls'

# exit
\q 



