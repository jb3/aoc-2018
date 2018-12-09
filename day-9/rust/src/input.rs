use std::fs::File;
use std::io::prelude::*;

pub fn get_input() -> (i64, i64) {
	let mut f = File::open("input.txt").expect("Could not open input.txt, is it present?");
	let mut buffer = String::new();

	f.read_to_string(&mut buffer).expect("Could not read to string, check file permissions?");

	let words = buffer.split(" ").collect::<Vec<&str>>();

	let number_of_players = words[0].parse::<i64>().expect("Could not get number of players, check input syntax.");
	let number_of_marbles = words[6].parse::<i64>().expect("Could not get number of players, check input syntax.");

	return (number_of_players, number_of_marbles);
}