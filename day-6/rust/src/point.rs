
#[derive(Debug, Copy, Clone)]
pub struct Point {
	pub x: i64,
	pub y: i64,
	pub infinite: bool,
	pub nearest_to: i64
}

impl Point {
	pub fn new(x: i64, y: i64) -> Point {
		Point{x, y, infinite: false, nearest_to: 0}
	}

	pub fn distance_from(&self, other_point: &Point) -> i32 {
		return ((self.x - other_point.x).abs() + (self.y - other_point.y).abs()) as i32;
	}
}