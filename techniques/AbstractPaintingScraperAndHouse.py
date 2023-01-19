from puzzles import AbstractPainting
from typing import Optional
from abc import abstractmethod
from Loc import Loc
class AbstractPaintingScraperAndHouse:
    @abstractmethod
    def solve1(self, puzzle: AbstractPainting, scraper: Optional[int], house: list[Loc]) -> int:
        raise NotImplementedError()

    def solve0(self, puzzle: AbstractPainting) -> int:
        edits = 0
        for index in range(len(puzzle)):
            row_house = puzzle.house_row(index)
            row_scraper = puzzle.east_scraper(index)
            edits += self.solve1(puzzle, row_scraper, row_house)
            col_house = puzzle.house_col(index)
            col_scraper = puzzle.south_scraper(index)
            edits += self.solve1(puzzle, col_scraper, col_house)
        for r in range(len(puzzle)):
            for c in range(len(puzzle)):
                loc = Loc(r, c)
                candidates = puzzle.cell_candidates(loc)
                if len(candidates) != 1:
                    continue
                fence = puzzle.cell_fence(loc)
                if 1 in candidates:
                    edits += puzzle.rem(puzzle.house_fence(fence), [0])
                if 0 in candidates:
                    edits += puzzle.rem(puzzle.house_fence(fence), [1])
        return edits