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


from puzzles import Mathrax
from tech import tech

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

    puzzle.solve([FinnedXWing()])

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
