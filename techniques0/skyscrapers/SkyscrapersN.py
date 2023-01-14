from Loc import Loc
from puzzles import Skyscrapers



class SkyscrapersN:
    def solve0(self, puzzle: Skyscrapers) -> int:
        edits = 0

        for index in range(len(puzzle)):
            north = puzzle.north_scraper(index)
            south = puzzle.south_scraper(index)
            east = puzzle.east_scraper(index)
            west = puzzle.west_scraper(index)

            if north == len(puzzle):
                edits += puzzle.rem([Loc(0, index)], set(puzzle.expected_candidates()).difference(
                    [min(puzzle.expected_candidates())]))

            if south == len(puzzle):
                edits += puzzle.rem([Loc(len(puzzle) - 1, index)], set(puzzle.expected_candidates()).difference(
                    [min(puzzle.expected_candidates())]))

            if west == len(puzzle):
                edits += puzzle.rem([Loc(index, 0)], set(puzzle.expected_candidates()).difference(
                    [min(puzzle.expected_candidates())]))

            if east == len(puzzle):
                edits += puzzle.rem([Loc(index, len(puzzle) - 1)], set(puzzle.expected_candidates()).difference(
                    [min(puzzle.expected_candidates())]))

        return edits


