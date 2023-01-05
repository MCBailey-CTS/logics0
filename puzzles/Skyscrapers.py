
from .Sumscrapers import Sumscrapers
from typing import Optional
from Loc import Loc

class Skyscrapers(Sumscrapers):
    def __init__(self, puzzle: str):
        super().__init__(puzzle)

    def _is_scraper_solved(self, sumscraper: Optional[int], house: list[Loc]) -> bool:
        solved_candidates = [self.cell_candidates(loc)[0] for loc in house if len(self.cell_candidates(loc)) == 1]
        if len(solved_candidates) != self.length:
            return False
        if sumscraper is None:
            return True

        current = 0
        max0 = 0

        for candidate in solved_candidates:
            if candidate < max0:
                continue
            current += 1
            max0 = candidate

        return sumscraper == current
