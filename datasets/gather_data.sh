#!/bin/bash

# filenames of datasets
SMALL='inail_small_orig.json'
MEDIUM='inail_medium_orig.json'
BIG='inail_big_orig.json'

# INAIL Open Data: work accidents
# Liguria region
# M/Y: 10-11-12/2019
url='https://dati.inail.it/api/OpenData/DatiConCadenzaMensileInfortuni?Regione=Liguria&AnnoAccadimento=2019&MeseAccadimento='
months=`seq 10 12`

# remove old copies of datasets
rm -rf inail*

echo -e '[' >> $SMALL
echo -e '[' >> $MEDIUM

for m in $months; do
	response=$(curl "$url$m")
	if [ $m -eq 11 ]; then
		echo -e "$response\n" >> $SMALL
	fi

	if [ $m -ne 12 ]; then
		echo -e "$response,\n" >> $MEDIUM
		echo -e "$response,\n" >> $BIG
	else
		echo -e "$response\n" >> $MEDIUM
		echo -e "$response\n" >> $BIG
	fi
done

big=$(cat $BIG)
echo -e '[' > $BIG
echo -e "$big,\n$big" >> $BIG

echo -e ']' >> $SMALL
echo -e ']' >> $MEDIUM
echo -e ']' >> $BIG
