import os
# import numpy as np

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

# def convert_to_sudoku_string(string: str

if __name__ == "__main__":
    temp0 = {1, 2, 3}
    temp1 = [6,7,8]

    print(temp0 + temp1)


    # return


    # for d in dir(Constants):
    #     if "sudoku" not in d:
    #         continue
    #     temp = getattr(Constants, d)
    #     result: str = temp()
    #     if "|" not in result:
    #         continue
    #     result = result.replace("|", "", -1) \
    #         .replace(" ", "", -1) \
    #         .replace("+", "", -1) \
    #         .replace('-', '', -1)
    #     string_array = []
    #     for i_line in result.split('\n'):
    #         line = i_line.strip()
    #         if len(line) == 0:
    #             continue
    #         string_array.append(line)
    #     _id = string_array.pop(0)
    #     length = int(string_array.pop(0))
    #     more = "".join(string_array).replace("0", ".", -1).replace("_", ".", -1)
    #     more = more[slice(81)]
    #     total_length = length * length
    #     # string = f'{length}\n'
    #     string = ''
    #     for index in range(length * length):
    #         if index % length == 0 and index != 0:
    #             string += '\n'
    #         string += f'{more[index]}'
    #
    #     string = string.replace("\n", "", -1).strip()
    #
    #     array_temp = []
    #
    #     for char in string:
    #         if char == '.':
    #             array_temp.append('123456789')
    #         elif char == '1':
    #             array_temp.append('1________')
    #         elif char == '2':
    #             array_temp.append('_2_______')
    #         elif char == '3':
    #             array_temp.append('__3______')
    #         elif char == '4':
    #             array_temp.append('___4_____')
    #         elif char == '5':
    #             array_temp.append('____5____')
    #         elif char == '6':
    #             array_temp.append('_____6___')
    #         elif char == '7':
    #             array_temp.append('______7__')
    #         elif char == '8':
    #             array_temp.append('_______8_')
    #         elif char == '9':
    #             array_temp.append('________9')
    #         else:
    #             raise Exception("bad sudoku char")
    #
    #         # elif(char == )
    #
    #     # for t in array_temp:
    #     #     print(t)
    #
    #     temper = []
    #
    #     count = 0
    #
    #     print('///////////')
    #     print('///////////')
    #     print('///////////')
    #     print('///////////')
    #     # for t in array_temp:
    #     #     print(t)
    #
    #     # x = np.array(array_temp)
    #
    #     x = np.reshape(array_temp, (length, length))
    #
    #     grid = []
    #     for t in x:
    #         k: list = t.tolist()
    #         grid.append(k)
    #
    #     string = f'{length}\n'
    #     for r in range(length):
    #         for c in range(length):
    #             string += f'{grid[r][c]}{sudoku_fences[r][c]} '
    #         string = string.strip()
    #         string += '\n'
    #
    #     print(string)
    #
    #
    #
    #
    #
    #     #
    #     #
    #     # print(x)
    #
    #     # print(_id)
    #     # print(_id)
    #     # # print(str(type(length)) + " " + str(length))
    #     # for index in range(length * length):
    #     #     print(array_temp[index], end=" ")
    #     #     if index % length == 0 and index != 0:
    #     #         print()
    #
    #
    #
    #         # cell = array_temp[index]
    #         # temper.append(cell)
    #         #
    #         # if index  % length == 0:
    #         #     # string += '\n'
    #         #     print(temper)
    #         #     temper = []
    #         # string += f'{more[index]}'
    #
    #     # print(char)
    #
    #     # print(_id)
    #     #
    #     #
    #     # print(string)
    #
    #     f = open(f"C:\\Users\\mcbailey\\Desktop\\files\\{_id}", "w")
    #     f.write(string)
    #     f.close()
