mod input;
mod player;

use std::collections::VecDeque;

#[derive(Debug)]
struct Marble {
	pub number: i64
}

fn main() {
    let (number_of_players, number_of_marbles) = input::get_input();

    let game_1 = play_game(number_of_players, number_of_marbles);
    println!("AoC part 1 answer: {}", game_1);

    let game_2 = play_game(number_of_players, number_of_marbles * 100);
    println!("AoC part 2 answer: {}", game_2);
}

fn play_game(player_count: i64, marble_count: i64) -> i64 {
	let mut players = vec![];
	let mut marbles = VecDeque::new();

	for i in 0..marble_count {
		marbles.push_back(Marble{number: i});
	}

	for _i in 0..player_count {
		players.push(player::Player::new());
	}

	let zero_marble = marbles.pop_front().unwrap();

	let mut circle = VecDeque::new();

	circle.push_front(zero_marble);
	
	let player_iterator = (0..player_count).into_iter().cycle();

	for player_number in player_iterator {
		let player = &mut players[player_number as usize];

		if marbles.len() == 0 {
			break
		}

		let marble = marbles.pop_front().unwrap();

		if marble.number % 23 == 0 {
			player.increase_score(marble.number);
			rotate_right(&mut circle, 7);
			let counter_seventh_marble: Marble = circle.pop_front().unwrap();
			player.increase_score(counter_seventh_marble.number);
			continue;
		}

		if circle.len() == 1 {
			circle.insert(1, marble);
		} else {
			circle.insert(2, marble);
		}

		rotate_left(&mut circle, 2);
	}

	let ts = top_scorer(&mut players);

	return ts.score;
}

fn rotate_right(marbles: &mut VecDeque<Marble>, rotations: usize) {
	for _ in 0..rotations {
		let back_popped = marbles.pop_back().unwrap();
		marbles.push_front(back_popped);
	}
}

fn rotate_left(marbles: &mut VecDeque<Marble>, rotations: usize) {
	for _ in 0..rotations {
		let front_popped = marbles.pop_front().unwrap();
		marbles.push_back(front_popped);
	}
}

fn top_scorer(players: &mut Vec<player::Player>) -> &player::Player {
	players.sort_unstable_by(|a, b| a.score.cmp(&b.score));

	return players.last().unwrap();
}