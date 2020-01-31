#!/bin/sh

DATA_DIR='datasets/inail_'
OUT_DIR='datasets/anon_'
DATASETS='small.json medium.json big.json'
K='4 5'
ALGS='P-F P-T'
CONFIG='configs.txt'
TMP_FILE='tmp'

# removing old temporary file if any
rm -f $TMP_FILE

echo 'Gathering data and statistics...'
for d in $DATASETS; do
	for k in $K; do
		for alg in $ALGS; do
			result=$(python3 main.py -i "$DATA_DIR$d" -o "$OUT_DIR$d" -a $alg -k $k -c $CONFIG)
			n_tuples=$(echo "$result" | grep Initial | cut -d'-' -f3 | tr -d '[:space:]')
			path_coverage=$(echo "$result" | grep Coverage | cut -d'-' -f3 | sed 's/.\{1\}$//' | tr -d '[:space:]')
			exec_time=$(echo "$result" | grep Overall | cut -d'-' -f3 | cut -d' ' -f1 | tr -d '[:space:]')
			echo "$n_tuples $path_coverage $exec_time $alg $k" >> $TMP_FILE
		done
	done
done

# launching the script that draw graphs for the presentation
python3 draw_graphics.py

# removing temporary file
rm -f $TMP_FILE
