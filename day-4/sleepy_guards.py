#!/usr/bin/env python

import datetime
import re
from dataclasses import dataclass

LOG_RE = re.compile(r"\[(\d{4})-(\d{2})-(\d{2})\ (\d{2}):(\d{2})] (.+)")
GUARD_SHIFT_RE = re.compile(r"Guard #(\d+) begins shift")

##########
# Part 1 #
##########


@dataclass
class LogEntry:
    year: int
    month: int
    day: int
    hour: int
    minute: int
    text: str

    def as_datetime(self) -> datetime.datetime:
        return datetime.datetime(int(self.year), int(self.month),
                                 int(self.day), int(self.hour),
                                 int(self.minute))

    @property
    def guard_number(self):
        if "Guard #" not in self.text:
            return None

        return int(GUARD_SHIFT_RE.match(self.text).groups()[0])

    @classmethod
    def from_log_entry(cls, text):
        match = LOG_RE.match(text)

        if match is None:
            raise Exception(f"Invalid log text: {text}")

        return cls(*match.groups())


with open("input.txt", "r") as f:
    guard_logs = f.readlines()

log_entries = []

for entry in guard_logs:
    log_entries.append(LogEntry.from_log_entry(entry))

log_entries = sorted(log_entries, key=lambda entry: entry.as_datetime())

active_guard = 0

asleep = {}

sleeps_at = None

for entry in log_entries:
    if "Guard #" in entry.text:
        active_guard = int(GUARD_SHIFT_RE.match(entry.text).groups()[0])

    if "falls asleep" in entry.text:
        sleeps_at = entry.as_datetime()

    if "wakes up" in entry.text:
        wakes_up = entry.as_datetime()
        slept_duration = wakes_up - sleeps_at
        slept_duration = (slept_duration.seconds / 60) - 1
        if active_guard not in asleep:
            asleep[active_guard] = 0

        asleep[active_guard] += slept_duration

most_sleepy_guard = sorted(asleep.items(),
                           key=lambda x: x[1],
                           reverse=True)[0][0]

active_guard = 0

slept_minutes = {}

sleeps_at = None

for entry in log_entries:
    if "Guard #" in entry.text:
        active_guard = int(GUARD_SHIFT_RE.match(entry.text).groups()[0])

    if active_guard != most_sleepy_guard:
        continue

    if "falls asleep" in entry.text:
        sleeps_at = entry.as_datetime()

    if "wakes up" in entry.text:
        wakes_at = entry.as_datetime()

        minutes_asleep = range(sleeps_at.minute, wakes_at.minute)

        for minute in minutes_asleep:
            if minute not in slept_minutes:
                slept_minutes[minute] = 0

            slept_minutes[minute] += 1

print(f"Sleepiest guard: {most_sleepy_guard}")

most_slept_minute = sorted(slept_minutes.items(),
                           key=lambda x: x[1],
                           reverse=True)[0]

print(f"Most slept minute: {most_slept_minute[0]} "
      f"({most_slept_minute[1]} days)")

aoc_answer_part_1 = most_sleepy_guard * most_slept_minute[0]

print(f"sleepiest guard * most slept minute = {aoc_answer_part_1}")

##########
# Part 2 #
##########

active_guard = 0

asleep = {}

sleeps_at = None

for entry in log_entries:
    if "Guard #" in entry.text:
        active_guard = int(GUARD_SHIFT_RE.match(entry.text).groups()[0])

    if "falls asleep" in entry.text:
        sleeps_at = entry.as_datetime()

    if "wakes up" in entry.text:
        wakes_up = entry.as_datetime()

        asleep_minutes = range(sleeps_at.minute, wakes_up.minute)

        if active_guard not in asleep:
            asleep[active_guard] = {}

        for minute in asleep_minutes:
            if minute not in asleep[active_guard]:
                asleep[active_guard][minute] = 0

            asleep[active_guard][minute] += 1

sorted_guards = {}

for guard, minutes in asleep.items():
    sorted_guards[guard] = sorted(minutes.items(),
                                  key=lambda x: x[1],
                                  reverse=True)

top_scorer = (0, (0, 0))

for guard in sorted_guards:
    if sorted_guards[guard][0][1] > top_scorer[1][1]:
        top_scorer = (guard, (sorted_guards[guard][0]))

print(f"Most frequent minute slept is Guard #{top_scorer[0]} at minute "
      f"{top_scorer[1][0]} ({top_scorer[1][1]}) days")

aoc_answer_part_2 = top_scorer[0] * top_scorer[1][0]

print(f"AOC Part 2 answer: {aoc_answer_part_2}")
