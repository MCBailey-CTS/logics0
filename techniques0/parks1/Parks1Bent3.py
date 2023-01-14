from Loc import Loc
from puzzles import Parks1


class Parks1Bent3:

    def solve0(self, puzzle: Parks1) -> int:
        edits = 0
        fence_dict = {}
        for r in range(len(puzzle)):
            for c in range(len(puzzle)):
                loc = Loc(r, c)
                fence = puzzle.cell_fence(loc)
                if fence not in fence_dict:
                    fence_dict[fence] = []
                fence_dict[fence].append(loc)

        for fence in fence_dict.keys():
            fence_locs = fence_dict[fence]
            solved_empty = [loc for loc in fence_locs if
                            len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 0]
            solved_tree = [loc for loc in fence_locs if
                           len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 1]
            unsolved = set(fence_locs).difference(solved_tree + solved_empty)
            if len(solved_tree) == 1:
                continue

            if len(unsolved) != 3:
                continue

            rows = set([loc.row for loc in unsolved])
            cols = set([loc.col for loc in unsolved])

            if len(rows) == 1 or len(cols) == 1:
                continue

            for pivot in unsolved:
                pincers = set(unsolved).difference([pivot])

                all_next_to = [loc.is_next_to(pivot) for loc in pincers]

                if not all(all_next_to):
                    continue

                # south-east
                if unsolved.issuperset([pivot.east(), pivot.south()]):
                    remove = [pivot.south().east()]

                    if pivot.north().is_valid_parks(puzzle.grid):
                        remove.append(pivot.north())

                    edits += puzzle.rem(remove, [1])

        return edits
