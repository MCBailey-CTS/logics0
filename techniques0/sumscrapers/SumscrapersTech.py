from Loc import Loc
from puzzles import Sumscrapers


class SumscrapersTech:
    def solve0(self, puzzle: Sumscrapers) -> int:
        edits = 0

        for index in range(len(puzzle)):
            north = puzzle.north_scraper(index)
            south = puzzle.south_scraper(index)
            east = puzzle.east_scraper(index)
            west = puzzle.west_scraper(index)

            if north == len(puzzle):
                edits += puzzle.rem([Loc(0, index)], set(puzzle.expected_candidates()).difference([len(puzzle)]))

            if south == len(puzzle):
                edits += puzzle.rem([Loc(len(puzzle) - 1, index)],
                                    set(puzzle.expected_candidates()).difference([len(puzzle)]))

            if east == len(puzzle):
                edits += puzzle.rem([Loc(index, len(puzzle) - 1)],
                                    set(puzzle.expected_candidates()).difference([len(puzzle)]))
            #
            if west == len(puzzle):
                edits += puzzle.rem([Loc(index, 0)],
                                    set(puzzle.expected_candidates()).difference([len(puzzle)]))

            total = sum(puzzle.expected_candidates())

            if south == total:
                expected = set(puzzle.expected_candidates())
                current = Loc(len(puzzle) - 1, index)
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
                current = Loc(0, len(puzzle) - 1)
                while len(expected) > 0:
                    min0 = min(expected)
                    # print(min0)
                    edits += puzzle.rem([current], set(puzzle.expected_candidates()).difference([min0]))
                    expected.remove(min0)
                    current = current.west()

        return edits


