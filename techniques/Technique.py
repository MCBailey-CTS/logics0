from abc import abstractmethod

class Technique:

    @abstractmethod
    def solve0(self, puzzle) -> int:
        raise NotImplementedError()

    def __repr__(self):
        return f'{self.__class__.__name__}()'

    @staticmethod
    def house_to_string(puzzle, house)->str:
        return "".join([puzzle.grid[loc.row][loc.col] for loc in house])
