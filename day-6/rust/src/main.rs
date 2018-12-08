#![feature(drain_filter)]

mod input;
mod point;

fn main() {

	//
	// Part 1
	//

    let mut points = input::get_input();

    let (min_x, max_x) = find_x_range(&mut points);
    let (min_y, max_y) = find_y_range(&mut points);

    for x in min_x..max_x + 1 {
    	for y in min_y..max_y + 1 {
    	    let point = point::Point::new(x, y);

    	    &points.sort_unstable_by(|a, b| a.distance_from(&point).cmp(&b.distance_from(&point)));

    	    if &points[0].distance_from(&point) == &points[1].distance_from(&point) {
    	    	continue
    	    }

    	    if point.x == min_x || point.x == max_x {
    	    	points[0].infinite = true;
    	    }

    	    if point.y == min_y || point.y == max_y {
    	    	points[0].infinite = true;
    	    }

    	    points[0].nearest_to += 1;
    	}
    }

    let mut non_infinite_points = points.drain_filter(|p| p.infinite == false).collect::<Vec<_>>();

    non_infinite_points.sort_unstable_by(|a, b| a.nearest_to.cmp(&b.nearest_to));

    println!("AoC part 1 answer: {}", non_infinite_points.last().unwrap().nearest_to);

    //
    // Part 2
    //

    let points = input::get_input(); // Let's reset the points for part 2

    let mut safe_area = 0;

    for x in min_x..max_x + 1 {
    	for y in min_y..max_y + 1 {
    	    let point = point::Point::new(x, y);

    	    let distances = points.iter().map(|p| p.distance_from(&point)).collect::<Vec<_>>();

    	    let sum_of_distances: i32 = distances.iter().sum();

    	    if sum_of_distances < 10000 {
    	    	safe_area += 1;
    	    }

    	}
    }

    println!("AoC part 2 answer: {}", safe_area);
}

fn find_x_range(points: &mut Vec<point::Point>) -> (i64, i64) {
	&points.sort_unstable_by(|a, b| a.x.cmp(&b.x));

	let max_x = points.last().unwrap().x;

	(points[0].x, max_x)
}

fn find_y_range(points: &mut Vec<point::Point>) -> (i64, i64) {
	&points.sort_unstable_by(|a, b| a.y.cmp(&b.y));

	let max_y = points.last().unwrap().y;

	(points[0].y, max_y)
}