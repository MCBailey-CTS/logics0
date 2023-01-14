from typing import Optional

from Loc import Loc
from puzzles import Sumscrapers


class SumscrapersSecondInLine:

    def solve0(self, puzzle: Sumscrapers) -> int:
        edits = 0

        tuples: list[tuple[Optional[int], list[Loc]]] = []

        for index in range(len(puzzle)):
            house = puzzle.house_row(index)
            tuples.append((puzzle.west_scraper(index), house))
            house = list(house)
            house.reverse()
            tuples.append((puzzle.east_scraper(index), house))
            house = puzzle.house_col(index)
            tuples.append((puzzle.north_scraper(index), house))
            house = list(house)
            house.reverse()
            tuples.append((puzzle.south_scraper(index), house))

        for tuple0 in tuples:
            scraper, house = tuple0
            if scraper is None:
                continue

            candidates1 = puzzle.cell_candidates(house[1])

            if len(candidates1) != 1:
                continue
            if candidates1[0] != len(puzzle):
                continue
            difference = scraper - len(puzzle)

            edits += puzzle.rem([house[0]], set(puzzle.expected_candidates()).difference([difference]))

            print(scraper)
            print(house)
        return edits

