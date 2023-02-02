

def first_or_def(__iterable, __predicate=None, __default=None)->any:
    return next(filter(__predicate, __iterable), __default)


def first(__iterable, __predicate=None)->any:
    return next(filter(__predicate, __iterable))

# if __name__ == "__main__":

#     temp = [1,3,5]



#     print(first_or_def(temp, lambda x: x % 2 == 0))
#     # print(first(temp))


def test_first_or_def():
    assert False

    