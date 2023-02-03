
import linq


def first_or_def(__iterable, __predicate=None, __default=None) -> any:
    tep = list()
    return next(filter(__predicate, __iterable), __default)


def first(__iterable, __predicate=None) -> any:
    return next(filter(__predicate, __iterable))


def single_or_def(__iterable, __predicate=None, __default=None) -> any:
    return next(filter(__predicate, __iterable), __default)


def single(__iterable, __predicate=None) -> any:
    return next(filter(__predicate, __iterable))


def to_dict_of_lists(__iterable, __key_selector) -> dict[any, list]:
    pass


def to_dict_of_sets(__iterable, __key_selector) -> dict[any, set]:
    pass


# if __name__ == "__main__":

#     temp = [1,3,5]


#     print(first_or_def(temp, lambda x: x % 2 == 0))
#     # print(first(temp))


def is_even(x):
    return x % 2 == 0


def test_first_or_def0(__iterable=(1, 3, 5, 6, 8), __predicate=is_even, expected=6):
    assert first_or_def(__iterable, __predicate) == expected


def test_first_or_def1(__iterable=(1, 3, 5), __predicate=is_even, expected=None):
    assert first_or_def(__iterable, __predicate) == expected


def test_single_or_def0(__iterable=(1, 3, 5, 6), __predicate=is_even, expected=6):
    assert single_or_def(__iterable, __predicate) == expected
