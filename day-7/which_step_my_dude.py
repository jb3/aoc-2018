#!/usr/bin/env python

from dataclasses import dataclass
from string import ascii_uppercase

from worker import Manager


steps = {}


@dataclass
class Step:
    dependencies: list
    dependents: list
    completed: bool = False
    assigned: bool = False

    def dependencies_satisfied(self):
        for dependency in self.dependencies:
            if steps[dependency].completed is False:
                return False

        return True


def parse_dependency(text: str) -> tuple:
    words = text.split(" ")

    # haha regex is dumb

    dependency = words[1]
    step = words[7]

    return step, dependency


with open("input.txt", "r") as f:
    step_dependencies = [l.strip() for l in f.readlines()]


for step in step_dependencies:
    step, dependency = parse_dependency(step)

    if step not in steps:
        steps[step] = Step([], [])

    steps[step].dependencies.append(dependency)

    if dependency not in steps:
        steps[dependency] = Step([], [])

    steps[dependency].dependents.append(step)

starting_step = sorted(
    filter(lambda x: len(x[1].dependencies) == 0, steps.items()), key=lambda r: r[0]
)[0]

print(f"Starting at {starting_step[0]}")

#
# NOTE: I completely fucked this stuff up and had to remove my part 1 solution
# to make part 2 even work lol.
#

manager = Manager(5)

ticks = 0

print(
    "Second",
    *[f"Worker[{i}]".rjust(15) for i in range(len(manager.workers))],
    "Done".rjust(15),
)

while True:
    if all([x[1].completed for x in steps.items()]):
        ticks -= 1
        break
    completed = manager.tick()

    for task in completed:
        steps[task].completed = True

    free_dependencies = filter(
        lambda x: x[1].dependencies_satisfied()
        and not x[1].completed
        and not x[1].assigned,
        steps.items(),
    )

    sorted_dependencies = sorted(list(free_dependencies), key=lambda x: x[0][0])

    if manager.free_workers():
        for dependency in sorted_dependencies:
            if manager.free_workers():
                manager.assign_work(
                    dependency[0][0], 60 + list(ascii_uppercase).index(dependency[0][0])
                )
                steps[dependency[0][0]].assigned = True
            else:
                break

    print(
        str(ticks).rjust(5),
        *[
            (worker.current_job if worker.current_job is not None else ".").rjust(15)
            for worker in manager.workers
        ],
        "".join([x[0][0] for x in steps.items() if x[1].completed is True]).rjust(15),
    )
    ticks += 1


print(f"AoC part 2 answer: {ticks}")
