from typing import Optional

from puzzles import Sumscrapers


class SumscrapersLastIsMax:

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

            candidates_n = puzzle.cell_candidates(house[puzzle.length - 1])

            if len(candidates_n) != 1:
                continue
            if candidates_n[0] != puzzle.length:
                continue

            difference = scraper - puzzle.length

            expected = set(puzzle.expected_candidates())

            expected.remove(puzzle.length)

            max0 = max(expected)

            if scraper == max0 + puzzle.length:
                edits += puzzle.rem([house[0]], set(puzzle.expected_candidates()).difference([max0]))
            else:
                edits += puzzle.rem([house[0]], [max0])
            # print(scraper)
            # print(house)
        return edits
