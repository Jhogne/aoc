#!/bin/bash
year="2021"
day="$(printf '%02d\n' $1)"
mod="pub mod day$day;"
match="$1 => (days::day$day::solve_1, days::day$day::solve_2),"

if (( day < 1 )); then
	exit 1 
fi

if [ ! -f src/days/day$day.rs ]; then
	cp "src/days/template.rs" "src/days/day$day.rs"
fi

if [ ! -f inputs/$1.txt ]; then
	curl --cookie "$AOC_COOKIE" "https://adventofcode.com/$year/day/$1/input" > inputs/$1.txt
fi

if ! grep -q "$mod" src/days/mod.rs; then
	echo "pub mod day$day;" >> "src/days/mod.rs"
fi

if ! grep -q "$match" src/main.rs; then
	sed -i "/unreachable!()/i \\\t \t$match" src/main.rs
fi
