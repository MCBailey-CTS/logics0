from Loc import Loc
from techniques.Technique import Technique
from colorama import Fore

class XyzWing(Technique):
    def solve0(self, puzzle) -> int:
        edits = 0
        for r in range(len(puzzle)):
            for c in range(len(puzzle)):
                pivot = Loc(r, c, puzzle.cell_fence(Loc(r,c)))
                pivot_candidates = puzzle.cell_candidates(pivot)
                if len(pivot_candidates) != 3:
                    continue
                row_locs = set([loc for loc in puzzle.house_row(pivot.row) if pivot != loc and len(puzzle.cell_candidates(loc)) == 2 ])
                fence_locs = [loc for loc in puzzle.house_fence(pivot.fence) if pivot != loc and len(puzzle.cell_candidates(loc)) == 2  ]
                for row_loc in row_locs:
                    row_candidates = puzzle.cell_candidates(row_loc)
                    if not set(pivot_candidates).issuperset(row_candidates):
                        continue
                    for fence_loc in fence_locs:
                        fence_candidates = puzzle.cell_candidates(fence_loc)
                        if not set(pivot_candidates).issuperset(fence_candidates):
                            continue
                        if set(row_candidates) == set(fence_locs):
                            continue
                        intersection = set(row_candidates).intersection(fence_candidates)
                        if len(intersection) != 1:
                            continue
                        remove = list(set(puzzle.house_fence(puzzle.cell_fence(fence_loc))).intersection(puzzle.house_row(row_loc.row)).difference([pivot]))
                        puzzle.override_loc_color(list(row_locs) + [fence_loc], Fore.YELLOW)
                        puzzle.override_loc_color([pivot], Fore.GREEN)
                        puzzle.override_loc_color(remove, Fore.RED)
                        edits += puzzle.rem(remove, intersection)

                col_locs = set([loc for loc in puzzle.house_col(pivot.col) if
                                pivot != loc and len(puzzle.cell_candidates(loc)) == 2])
                fence_locs = [loc for loc in puzzle.house_fence(pivot.fence) if
                              pivot != loc and len(puzzle.cell_candidates(loc)) == 2]
                for row_loc in col_locs:
                    row_candidates = puzzle.cell_candidates(row_loc)
                    if not set(pivot_candidates).issuperset(row_candidates):
                        continue
                    for fence_loc in fence_locs:
                        fence_candidates = puzzle.cell_candidates(fence_loc)
                        if not set(pivot_candidates).issuperset(fence_candidates):
                            continue
                        if set(row_candidates) == set(fence_locs):
                            continue
                        intersection = set(row_candidates).intersection(fence_candidates)
                        if len(intersection) != 1:
                            continue
                        remove = list(set(puzzle.house_fence(puzzle.cell_fence(fence_loc))).intersection(
                            puzzle.house_col(row_loc.col)).difference([pivot]))
                        puzzle.override_loc_color(list(col_locs) + [fence_loc], Fore.YELLOW)
                        puzzle.override_loc_color([pivot], Fore.GREEN)
                        puzzle.override_loc_color(remove, Fore.RED)
                        edits += puzzle.rem(remove, intersection)
        return edits