use std::fs::File;
use std::io::prelude::*;
use crate::point::Point;

pub fn get_input() -> Vec<Point> {
	let input = open_input_file();

	let split_lines = split_input_lines(input);

	coords_to_points(split_lines)
}

fn open_input_file() -> String {
	let mut f = File::open("input.txt").expect("Could not open input.txt, is it present?");
    let mut buffer = String::new();

    f.read_to_string(&mut buffer).expect("Could not read from input.txt, check permissions.");

    buffer
}

fn split_input_lines(input: String) -> Vec<String> {
	let mut lines_iter = input.lines();

	let mut lines: Vec<String> = vec![];

	loop {
		if let Some(line) = lines_iter.next() {
			lines.push(String::from(line));
		} else {
			break;
		}
	}

	lines
}

fn coords_to_points(lines: Vec<String>) -> Vec<Point> {
	let mut points: Vec<Point> = vec![];

	for line in lines {
		let v = line.split(", ").collect::<Vec<&str>>();
		let x: i64 = v[0].parse::<i64>().unwrap();
		let y: i64 = v[1].parse::<i64>().unwrap();
		points.push(Point::new(x, y));
	}

	points
}