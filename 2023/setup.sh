#!/bin/bash
year="2023"
day="$(printf '%02d\n' $1)"

if (( day < 1 || day > 25)); then
	exit 1 
fi

mkdir $day
if [ ! -f $day/main.py ]; then
	cp .template.py $day/main.py
fi

if [ ! -f $day/input.txt ]; then
	curl --cookie $(cat "$XDG_DATA_HOME/aoc/cookie") "https://adventofcode.com/$year/day/$1/input" > $day/input.txt
fi
