import os
from typing import Iterable

import numpy

import temp
# import numpy as np
# from py_linq import Enumarable
from Constants import Constants
from Loc import Loc
from puzzles import Kropki

from linq import linq
from techniques.FinnedXWing import FinnedXWing
from techniques.HiddenSingle import HiddenSingle
from techniques.UniqueRectangleType4 import UniqueRectangleType4

sudoku_fences = [
    ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'],
    ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'],
    ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'],
    ['d', 'd', 'd', 'e', 'e', 'e', 'f', 'f', 'f'],
    ['d', 'd', 'd', 'e', 'e', 'e', 'f', 'f', 'f'],
    ['d', 'd', 'd', 'e', 'e', 'e', 'f', 'f', 'f'],
    ['g', 'g', 'g', 'h', 'h', 'h', 'i', 'i', 'i'],
    ['g', 'g', 'g', 'h', 'h', 'h', 'i', 'i', 'i'],
    ['g', 'g', 'g', 'h', 'h', 'h', 'i', 'i', 'i'],
]


def replace_sudoku():
    for d in dir(Constants):
        if "sudoku" not in d:
            continue
        temp = getattr(Constants, d)
        result: str = temp()
        if "|" not in result:
            continue
        result = result.replace("|", "", -1) \
            .replace(" ", "", -1) \
            .replace("+", "", -1) \
            .replace('-', '', -1)
        string_array = []
        for i_line in result.split('\n'):
            line = i_line.strip()
            if len(line) == 0:
                continue
            string_array.append(line)
        _id = string_array.pop(0)
        length = int(string_array.pop(0))
        more = "".join(string_array).replace("0", ".", -1).replace("_", ".", -1)
        more = more[slice(81)]
        total_length = length * length
        # string = f'{length}\n'
        string = ''
        for index in range(length * length):
            if index % length == 0 and index != 0:
                string += '\n'
            string += f'{more[index]}'

        string = string.replace("\n", "", -1).strip()

        array_temp = []

        for char in string:
            if char == '.':
                array_temp.append('123456789')
            elif char == '1':
                array_temp.append('1________')
            elif char == '2':
                array_temp.append('_2_______')
            elif char == '3':
                array_temp.append('__3______')
            elif char == '4':
                array_temp.append('___4_____')
            elif char == '5':
                array_temp.append('____5____')
            elif char == '6':
                array_temp.append('_____6___')
            elif char == '7':
                array_temp.append('______7__')
            elif char == '8':
                array_temp.append('_______8_')
            elif char == '9':
                array_temp.append('________9')
            else:
                raise Exception("bad sudoku char")

            # elif(char == )

        # for t in array_temp:
        #     print(t)

        temper = []

        count = 0

        print('///////////')
        print('///////////')
        print('///////////')
        print('///////////')
        # for t in array_temp:
        #     print(t)

        # x = np.array(array_temp)

        x = np.reshape(array_temp, (length, length))

        grid = []
        for t in x:
            k: list = t.tolist()
            grid.append(k)

        string = f'{length}\n'
        for r in range(length):
            for c in range(length):
                string += f'{grid[r][c]}{sudoku_fences[r][c]} '
            string = string.strip()
            string += '\n'

        print(string)

        #
        #
        # print(x)

        # print(_id)
        # print(_id)
        # # print(str(type(length)) + " " + str(length))
        # for index in range(length * length):
        #     print(array_temp[index], end=" ")
        #     if index % length == 0 and index != 0:
        #         print()

        # cell = array_temp[index]
        # temper.append(cell)
        #
        # if index  % length == 0:
        #     # string += '\n'
        #     print(temper)
        #     temper = []
        # string += f'{more[index]}'

        # print(char)

        # print(_id)
        #
        #
        # print(string)

        f = open(f"C:\\Users\\mcbailey\\Desktop\\files\\{_id}", "w")
        f.write(string)
        f.close()


# def convert_to_sudoku_string(string: str

def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]] + item
            yield item


def powert_set_start():
    temp = [0, 1, 2, 6, 6, 7]

    array = [
        [0, 1, 3, 8],
        [5],
        [0, 1, 2, 4, 8]
    ]

    r = [x for x in powerset(temp) if len(x) == 2]
    r.sort()
    print(r)


# def where(function, iterable):
#     return filter(function, iterable)

# def is_even(x):
#     return 


# def first

# def to_set(self)->set:
#     return

# def select(self, func=lambda x: x):
#     pass

def read_sudokus():
    for name in dir(Constants):
        if 'sudoku' in name and 'explicit' in name:
            func = getattr(Constants, name)
            string: str = func()
            string = string.replace('\n', ' ', -1).replace('  ', ' ', -1).replace('  ', ' ', -1).replace('  ', ' ',
                                                                                                         -1).replace(
                '  ', ' ', -1).strip()
            split = string.split(' ')
            _id = split.pop(0)

            try:
                length = int(split.pop(0))
                # print(_id)
                # print(length)
                # print(split)

                if length != 9:
                    continue
                index = 0
                result = f'{length} $ $ $ $ $ $ $ $\n'
                for r in range(length):
                    if r == 3 or r == 6:
                        result += '\n'
                    for c in range(length):
                        result += f'{split[index]} '
                        index += 1
                        if c == 2 or c == 5:
                            result += '   '
                    result += '\n'

                result.strip()

                f = open(f'C:\\Users\\mcbailey\\Desktop\\files\\{_id}', 'w')

                f.write(result)

                f.close()

                # print(result)
                # print()
                # print()
                # print()


            except:
                print(f'Exception: bad string format: {_id}')


def temperature():
    for name in dir(temp):
        if '__' in name:
            continue
        # print(name)
        string: str = getattr(temp, name)()
        string = string.replace(' ', '', -1) \
            .replace(' ', '', -1) \
            .replace(' ', '', -1) \
            .replace(' ', '', -1) \
            .replace(' ', '', -1) \
            .replace(' ', '', -1) \
            .replace(' ', '', -1) \
            .replace(' ', '', -1) \
            .replace('|', '', -1) \
            .replace('-', '', -1) \
            .replace('+', '', -1)
        split = string.split('\n')

        array = []
        for temp1 in split:
            strip = temp1.strip()

            if len(strip) == 0:
                continue
            array.append(strip)

        puzzle_id = array.pop(0)
        length = int(array.pop(0))

        separate = [int(char) for char in "".join(array).replace('.', '0', -1).replace('_', '0', -1)]

        if len(separate) != 81:
            continue

        hello = numpy.array(separate)

        hello = hello.reshape(9, 9)

        actual_array = numpy.empty([9, 9], dtype=object)

        for r in range(9):
            for c in range(9):
                if hello[r][c] == 0:
                    actual_array[r][c] = f'123456789{sudoku_fences[r][c]}'
                    continue
                string = ''
                for candidate in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    if candidate == hello[r][c]:
                        string += f'{candidate}'
                    else:
                        string += f'_'
                string += sudoku_fences[r][c]
                actual_array[r][c] = string

        puzzle_string = f'{9} $ $ $ $ $ $ $ $\n'
        for r in range(9):
            if r == 3 or r == 6:
                puzzle_string += '\n'
            for c in range(9):
                if c == 3 or c == 6:
                    puzzle_string += '  '
                puzzle_string += f'{actual_array[r][c]} '
            puzzle_string += '\n'

        f = open(f'C:\\Users\\mcbailey\\Desktop\\files\\{puzzle_id}', 'w')

        f.write(puzzle_string)
        f.close()


from puzzles import Sudoku
from colorama import Fore


class FinnedXWing1:

    def solve1(self, puzzle: Sudoku, __col0, __col1, __candidate) -> int:
        edits = 0
        containing_locs0 = [loc for loc in __col0 if __candidate in puzzle.cell_candidates(loc)]
        containing_locs1 = [loc for loc in __col1 if __candidate in puzzle.cell_candidates(loc)]

        containing_locs = containing_locs0 + containing_locs1

        # print(containing_locs)

        rows = set(loc.row for loc in containing_locs)
        cols = set(loc.col for loc in containing_locs)
        row_chutes = set(puzzle.row_chute(loc) for loc in containing_locs)
        col_chutes = set(puzzle.col_chute(loc) for loc in containing_locs)

        fence_dict = {}
        for loc in containing_locs:
            fence = puzzle.cell_fence(loc)
            if fence not in fence_dict:
                fence_dict[fence] = set()
            fence_dict[fence].add(loc)

        chute_dict = {}
        for loc in containing_locs:
            chute = puzzle.loc_chute(loc)
            if chute not in chute_dict:
                chute_dict[chute] = set()
            chute_dict[chute].add(loc)

        count_length_1 = set(chute_fence for chute_fence in chute_dict.keys() if len(chute_dict[chute_fence]) == 1)
        count_length_more_than_1 = set(
            chute_fence for chute_fence in chute_dict.keys() if len(chute_dict[chute_fence]) > 1)

        if (len(rows) == 2 or len(cols) == 2) and \
                len(fence_dict) == 4 and \
                len(row_chutes) == 2 and \
                len(col_chutes) == 2 and \
                len(chute_dict) == 4 and \
                len(count_length_1) == 3 and \
                len(count_length_more_than_1) == 1:
            chute_with_fin = list(count_length_more_than_1)[0]
            fence = puzzle.fence_from_chute(chute_with_fin)
            puzzle.override_loc_color(puzzle.house_fence(fence), Fore.BLUE)

            puzzle.override_loc_color(containing_locs, Fore.YELLOW)
            next_to_chutes = [chute for chute in count_length_1 if
                              chute_with_fin.in_same_row(chute) or chute_with_fin.in_same_col(chute)]
            locs_in_next_to_chute = []
            for chute in next_to_chutes:
                locs_in_next_to_chute.append(
                    set(containing_locs).intersection(puzzle.house_fence(puzzle.fence_from_chute(chute))))
            locs_in_fin_chute = set(containing_locs).intersection(puzzle.house_fence(fence))
            puzzle.override_loc_color(list(locs_in_fin_chute), Fore.YELLOW)
            for loc_chute in locs_in_next_to_chute:
                temp = list(loc_chute)[0]

                row_intersection = set(puzzle.house_row(temp.row)).intersection(puzzle.house_fence(fence)).difference(
                    containing_locs)
                col_intersection = set(puzzle.house_col(temp.col)).intersection(puzzle.house_fence(fence)).difference(
                    containing_locs)

                remove = list(row_intersection) + list(col_intersection)

                puzzle.override_loc_color(remove, Fore.RED)

                edits += puzzle.rem(remove, [__candidate])

                if edits > 0:
                    return edits

        return edits

    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0
        for candidate in puzzle.expected_candidates():
            for i in range(0, len(puzzle) - 1):
                for ii in range(i + 1, len(puzzle)):
                    edits += self.solve1(puzzle, puzzle.house_row(i), puzzle.house_row(ii), candidate)
                    edits += self.solve1(puzzle, puzzle.house_col(i), puzzle.house_col(ii), candidate)

        return edits


from puzzles import Mathrax
from tech import tech


def is_valid_finned(containing_locs: list[Loc]) -> bool:
    puzzle.override_loc_color(containing_locs, Fore.YELLOW)
    rows = set(loc.row for loc in containing_locs)
    cols = set(loc.col for loc in containing_locs)
    row_chutes = set(puzzle.row_chute(loc) for loc in containing_locs)
    col_chutes = set(puzzle.col_chute(loc) for loc in containing_locs)

    fence_dict = {}
    for loc in containing_locs:
        fence = puzzle.cell_fence(loc)
        if fence not in fence_dict:
            fence_dict[fence] = set()
        fence_dict[fence].add(loc)

    chute_dict = {}
    for loc in containing_locs:
        chute = puzzle.loc_chute(loc)
        if chute not in chute_dict:
            chute_dict[chute] = set()
        chute_dict[chute].add(loc)

    count_length_1 = set(chute_fence for chute_fence in chute_dict.keys() if len(chute_dict[chute_fence]) == 1)
    count_length_more_than_1 = set(
        chute_fence for chute_fence in chute_dict.keys() if len(chute_dict[chute_fence]) > 1)

    length_1_locs = [list(t)[0] for t in count_length_1]

    print(length_1_locs)

    if (len(rows) == 2 or len(cols) == 2) and \
            len(fence_dict) == 4 and \
            len(row_chutes) == 2 and \
            len(col_chutes) == 2 and \
            len(chute_dict) == 4 and \
            len(count_length_1) == 3 and \
            len(count_length_more_than_1) == 1:
        chute_with_fin = list(count_length_more_than_1)[0]
        fence = puzzle.fence_from_chute(chute_with_fin)
        puzzle.override_loc_color(puzzle.house_fence(fence), Fore.BLUE)
    return False


if __name__ == "__main__":
    from os import walk

    f = open('C:\\repos\\logics0\\solve_files\\' + "finned_x_wing_00.sudoku", 'r')
    from puzzles import Sudoku

    string = f'id.sudoku\n{f.read()}'.replace('$', '', -1)
    f.close()

    # print(string)

    puzzle = Sudoku(string)
    from techniques.CrossHatch import CrossHatch

    puzzle.solve([CrossHatch(), HiddenSingle(), tech.LockedCandidatesPointing(),
                  # UniqueRectangleType4()
                  ])
    # puzzle.solve([CrossHatch(), HiddenSingle(), tech.LockedCandidatesPointing()])
    # puzzle.solve([HiddenSingle()])
    # puzzle.solve([tech.LockedCandidatesPointing()])
    # puzzle.solve([CrossHatch()])
    # puzzle.solve([UniqueRectangleType4()])

    # puzzle.solve([FinnedXWing1()])

    right = [Loc(5, 3), Loc(6, 3)]
    left = [Loc(4, 2), Loc(5, 2), Loc(6, 2)]

    corners = right + left

    candidate = 2

    # puzzle.override_loc_color(corners, Fore.YELLOW)
    puzzle.override_loc_color(right, Fore.GREEN)

    in_cols = True

    for i in range(len(puzzle)):
        if in_cols and right[0].col != i:
            other_col = puzzle.house_col(i, candidate)
            if len(other_col) == 3:
                # puzzle.override_loc_color(other_col, Fore.YELLOW)
                puzzle.override_loc_color(right, Fore.YELLOW)


                # intersection = set(other_col).intersection()
                #
                # fin = intersection.difference(other_col)
                #
                # puzzle.override_loc_color(fin, Fore.BLUE)




    # is_valid_finned()

    print(puzzle.to_string())

    # files = []
    # for filename in next(walk('C:\\Users\\mcbailey\\Desktop\\files'), (None, None, []))[2]:  # [] if no file
    #     print(f"""'{filename}': [],""")
    # if 'actual' in filename:
    # files.append(filename)

    #
    #     # print(puzzle_string)
    #
    #     # print(actual_array)
    #     #
    #     #
    #     # numpy.savetxt(f'C:\\Users\\mcbailey\\Desktop\\files\\{puzzle_id}.sudoku',2,actual_array)
