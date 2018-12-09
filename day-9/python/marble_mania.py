#!/usr/bin/env python

import itertools
from collections import deque, namedtuple

with open("input.txt", "r") as f:
    inp = f.read().split()

    number_of_players = int(inp[0])
    number_of_marbles = int(inp[6])

Marble = namedtuple("Marble", "number")


class Player:
    def __init__(self):
        self.score = 0


def play_game(player_count, marble_count):
    players = deque([])
    marbles = deque([Marble(number=i + 1) for i in range(marble_count)])

    for i in range(player_count):
        players.append(Player())

    circle = deque([Marble(number=0)])

    for turn in itertools.cycle(range(player_count)):
        player = players[turn]

        if len(marbles) == 0:
            break

        marble = marbles.popleft()

        if marble.number % 23 == 0:
            player.score += marble.number

            circle.rotate(7)
            counter_seventh_marble = circle.popleft()
            player.score += counter_seventh_marble.number
            continue

        circle.insert(2, marble)
        circle.rotate(-2)

    highest_scoring_players = sorted(players,
                                     key=lambda p: p.score,
                                     reverse=True)
    return highest_scoring_players


if __name__ == "__main__":
    highest_scoring_players = play_game(number_of_players, number_of_marbles)
    print(f"AoC part 1 answer: {highest_scoring_players[0].score}")

    highest_scoring_players_2 = play_game(number_of_players,
                                          number_of_marbles * 100)
    print(f"AoC part 2 answer: {highest_scoring_players_2[0].score}")
