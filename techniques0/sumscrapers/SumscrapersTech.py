from Loc import Loc
from puzzles import Sumscrapers


class SumscrapersTech:
    def solve0(self, puzzle: Sumscrapers) -> int:
        edits = 0

        for index in range(puzzle.length):
            north = puzzle.north_scraper(index)
            south = puzzle.south_scraper(index)
            east = puzzle.east_scraper(index)
            west = puzzle.west_scraper(index)

            if north == puzzle.length:
                edits += puzzle.rem([Loc(0, index)], set(puzzle.expected_candidates()).difference([puzzle.length]))

            if south == puzzle.length:
                edits += puzzle.rem([Loc(puzzle.length - 1, index)],
                                    set(puzzle.expected_candidates()).difference([puzzle.length]))

            if east == puzzle.length:
                edits += puzzle.rem([Loc(index, puzzle.length - 1)],
                                    set(puzzle.expected_candidates()).difference([puzzle.length]))
            #
            if west == puzzle.length:
                edits += puzzle.rem([Loc(index, 0)],
                                    set(puzzle.expected_candidates()).difference([puzzle.length]))

            total = sum(puzzle.expected_candidates())

            if south == total:
                expected = set(puzzle.expected_candidates())
                current = Loc(puzzle.length - 1, index)
                while len(expected) > 0:
                    min0 = min(expected)
                    edits += puzzle.rem([current], set(puzzle.expected_candidates()).difference([min0]))
                    expected.remove(min0)
                    current = current.north()

            # if north == total:
            #     expected = set(puzzle.expected_candidates())
            #     current = Loc(0, index)
            #     while len(expected) > 0:
            #         min0 = min(expected)
            #         edits += puzzle.rem([current], set(puzzle.expected_candidates()).difference([min0]))
            #         expected.remove(min0)
            #         current = current.south()

            if east == total:
                expected = set(puzzle.expected_candidates())
                current = Loc(0, puzzle.length - 1)
                while len(expected) > 0:
                    min0 = min(expected)
                    # print(min0)
                    edits += puzzle.rem([current], set(puzzle.expected_candidates()).difference([min0]))
                    expected.remove(min0)
                    current = current.west()

        return edits


