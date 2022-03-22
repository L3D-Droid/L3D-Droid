#!/bin/bash

file=crest_conformers.xyz
i=1
while read line; do
	i=$((i+1))	       
done<$file

b=$i




for line in file
do
	read line
	echo "No. of atoms in the Molecule = "$line
done<$file
d=$line
c=$(($((b-1))/$((d+2))))


cp crest_conformers.xyz 1.xyz
python3.6 sample_1.py 1.xyz
sed -i s/" $line"/" "/g *.gjf

echo -e "\n" >> AR400_$c.gjf

rm 1.xyz
