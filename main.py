import os
from typing import Iterable
# import numpy as np
# from py_linq import Enumarable
from Constants import Constants

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



class linq(list):
    def __init__(self, __iterable: Iterable):
        super().__init__(__iterable)
        
    def any(self, predicate)->bool:
        return any(item for item in self if predicate(item))

    def all(self, predicate)->bool:
        return all(item for item in self if predicate(item))
    def where(self, func):
        return linq(item for item in self if func(item))        

    def select(self, func):
        return linq(func(item) for item in self)        

    def __single(self):
        if len(self) == 1:
            return self[0]
        if len(self) == 0:
            raise Exception('empty sequence')
        raise Exception('more than one element')

    def __single_func(self, predicate):
        return linq([item for item in self if predicate(item)]).__single()
    def single(self, predicate=None):
        return self.__single_func(predicate) if predicate is not None else self.__single()


    def __single_or_none(self):
        if len(self) != 1:
            raise Exception('more than one element')
        return self[0]

    def __single_func_or_none(self, predicate):
        return linq([item for item in self if predicate(item)]).__single_or_none()
    def single_or_none(self, predicate=None):
        return self.__single_func_or_none(predicate) if predicate is not None else self.__single_or_none()


    # def first

    # def to_set(self)->set:
    #     return 

    # def select(self, func=lambda x: x):
    #     pass

if __name__ == "__main__":
    # from linq import linq
    temp = linq([1,2,3,4,5])

    print(temp.single(lambda x:x==2))



    # temp.

    # print(set(temp.where(lambda x :x % 2 == 0)))