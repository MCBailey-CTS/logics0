from typing import Optional

from Loc import Loc
from _puzzles import Sumscrapers


class SumscrapersNextToScraper:

    def solve0(self, puzzle: Sumscrapers) -> int:
        edits = 0

        tuples: list[tuple[Optional[int], list[Loc]]] = []

        for index in range(puzzle.length):
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

            if scraper > puzzle.length:
                edits += puzzle.rem([house[0]], [puzzle.length])

        return edits