from typing import Iterable

class linq(Iterable):
    def __init__(self, __iterable: Iterable):
        super().__init__(__iterable)
        
    @overload
    def any(self, predicate)->bool:
        return any(item for item in self if predicate(item))

    def all(self, predicate)->bool:
        return all(item for item in self if predicate(item))
        
    def where(self, predicate):
        return linq(item for item in self if predicate(item))        

    def select(self, func)->'linq':
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

    





# select
# order_by
# order_by_descending
# skip
# take
# where
# select_many
# add
# concat
# join
# intersect
# except_
# to_list
# count
# sum
# min
# max
# avg
# median
# any
# element_at
# element_at_or_default
# first
# first_or_default
# last
# last_or_default
# contains
# group_by
# distinct
# group_join
# union
# all
# aggregate
# append
# prepend
# empty
# range
# repeat
# reverse
# skip_last
# skip_while
# take_last
# take_while
# zip
# default_if_empty
# single
# single_or_default
# to_dictionary


