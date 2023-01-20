from abc import abstractmethod

class Technique:

    @abstractmethod
    def solve0(self, puzzle) -> int:
        raise NotImplementedError()

    def __repr__(self):
        return f'{self.__class__.__name__}()'
