from Loc import Loc
from puzzles import Skyscrapers



class SkyscrapersN:
    def solve0(self, puzzle: Skyscrapers) -> int:
        edits = 0

        for index in range(puzzle.length):
            north = puzzle.north_scraper(index)
            south = puzzle.south_scraper(index)
            east = puzzle.east_scraper(index)
            west = puzzle.west_scraper(index)

            if north == puzzle.length:
                edits += puzzle.rem([Loc(0, index)], set(puzzle.expected_candidates()).difference(
                    [min(puzzle.expected_candidates())]))

            if south == puzzle.length:
                edits += puzzle.rem([Loc(puzzle.length - 1, index)], set(puzzle.expected_candidates()).difference(
                    [min(puzzle.expected_candidates())]))

            if west == puzzle.length:
                edits += puzzle.rem([Loc(index, 0)], set(puzzle.expected_candidates()).difference(
                    [min(puzzle.expected_candidates())]))

            if east == puzzle.length:
                edits += puzzle.rem([Loc(index, puzzle.length - 1)], set(puzzle.expected_candidates()).difference(
                    [min(puzzle.expected_candidates())]))

        return edits


