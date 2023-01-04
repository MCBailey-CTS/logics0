import os

from Constants import Constants

sudoku_fences = [
    ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'],
    ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'],
    ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'],
    ['d', 'd', 'd', 'e', 'e', 'e', 'f', 'f', 'f'],
    ['d', 'd', 'd', 'e', 'e', 'e', 'f', 'f', 'f'],
    ['d', 'd', 'd', 'e', 'e', 'e', 'f', 'f', 'f'],
    ['g', 'g', 'g', 'h', 'h', 'h', 'i', 'i', 'i'],
]

# def convert_to_sudoku_string(string: str

if __name__ == "__main__":
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
        string = f'{length}\n'
        for index in range(length * length):
            if index % length == 0 and index != 0:
                string += '\n'
            string += f'{more[index]}'

        # print(_id)
        #
        #
        # print(string)

        f = open(f"C:\\Users\\mcbailey\\Desktop\\files\\{_id}", "w")
        f.write(string)
        f.close()
