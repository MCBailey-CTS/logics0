
from Loc import Loc
from _puzzles import Skyscrapers
from typing import Optional
class SkyscrapersRange:
    def solve0(self, puzzle: Skyscrapers) -> int:
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

            string = "".join([puzzle.grid[loc.row][loc.col] for loc in house])

            if string == "1____23__23____4" and scraper == 4:
                edits += puzzle.rem([house[1]], [3])

            if string == "1____23__23____4" and scraper == 3:
                edits += puzzle.rem([house[1]], [2])

            if string == "123_1_3_12_____4" and scraper == 2:
                edits += puzzle.rem([house[0]], [1, 2, 4])

            if string == "123_123_123____4" and scraper == 2:
                edits += puzzle.rem([house[0]], [1, 2, 4])

            if string == "12__12_____4__3_" and scraper == 3:
                edits += puzzle.rem([house[0]], [1])

            if string == "_23__23____41___" and scraper == 3:
                edits += puzzle.rem([house[0]], [3])

            if string == "_23__23____41___" and scraper == 2:
                edits += puzzle.rem([house[0]], [2])

            if string == "123_123_123____4" and scraper == 3:
                edits += puzzle.rem([house[0]], [3])

            if string == "123_123_12341234" and scraper == 3:
                edits += puzzle.rem([house[0]], [3])

            if string == "12__12____3____4" and scraper == 3:
                edits += puzzle.rem([house[0]], [1])

            if string == "_2_4_2_41_____3_" and scraper == 2:
                edits += puzzle.rem([house[0]], [4])

            if string == "1_3__2_____41_3_" and scraper == 2:
                edits += puzzle.rem([house[0]], [1])

            if string == "1234123412341234" and scraper == 3:
                edits += puzzle.rem([house[0]], [4])

            if string == "1234123412341234" and scraper == 2:
                edits += puzzle.rem([house[0]], [4])

        # 1___ ___4 _23_ _23_

        # print(string)

        # house_candidates = [puzzle.cell_candidates(loc) for loc in house]
        # for index in range(puzzle.length):
        #     candidates = house_candidates[index]
        #     if len(candidates) != 1:
        #         continue
        #     solved_candidate = candidates[0]
        #     if solved_candidate != puzzle.length:
        #         continue
        #     if index == 0 or index == puzzle.length - 1:
        #         continue
        #
        #
        #     print("her111r")

        # candidates1 = puzzle.cell_candidates(house[1])
        #
        # if len(candidates1) != 1:
        #     continue
        # if candidates1[0] != puzzle.length:
        #     continue
        # difference = scraper - puzzle.length
        #
        # edits += puzzle.rem([house[0]], set(puzzle.expected_candidates()).difference([difference]))

        return edits
