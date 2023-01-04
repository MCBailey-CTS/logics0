from Loc import Loc
from _puzzles import Skyscrapers


class Skyscrapers1:
        def solve0(self, puzzle: Skyscrapers) -> int:
            edits = 0

            for index in range(puzzle.length):
                north = puzzle.north_scraper(index)
                south = puzzle.south_scraper(index)
                east = puzzle.east_scraper(index)
                west = puzzle.west_scraper(index)

                if north == 1:
                    edits += puzzle.rem([Loc(0, index)], set(puzzle.expected_candidates()).difference(
                        [max(puzzle.expected_candidates())]))

                if south == 1:
                    edits += puzzle.rem([Loc(puzzle.length - 1, index)], set(puzzle.expected_candidates()).difference(
                        [max(puzzle.expected_candidates())]))

                if west == 1:
                    edits += puzzle.rem([Loc(index, 0)], set(puzzle.expected_candidates()).difference(
                        [max(puzzle.expected_candidates())]))

                if east == 1:
                    edits += puzzle.rem([Loc(index, puzzle.length - 1)], set(puzzle.expected_candidates()).difference(
                        [max(puzzle.expected_candidates())]))

            return edits
