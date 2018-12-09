#[derive(Debug)]
pub struct Player {
	pub score: i64
}

impl Player {
	pub fn new() -> Player {
		Player{score: 0}
	}

	pub fn increase_score(&mut self, points: i64) {
		self.score += points;
	}
}