class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.inner_list = self.list_of_list.pop(0)
        return self

    def get_inner_list(self):
        if len(self.list_of_list) != 0:
            self.inner_list = self.list_of_list.pop(0)
        else:
            raise StopIteration
        return self

    def __next__(self):
        if len(self.inner_list) == 0:
            self.get_inner_list()
        return self.inner_list.pop(0)
def test_1(): # этот тест не проходит, хотя код работает на разных примерах. Это надо знать принцип работы тестов,
    # чтобы подгонять код как это было в одном из модулей на встроенных тренажерах. Либо можете привести пример
    #  исходных данных, при котором код работать не будет.
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]



import types
def flat_generator(list_of_lists):
    for item in list_of_lists:
            yield from item

def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


def foo(data, res=[]):  # здесь не получается сделать через yield чтобы каждое значение
    # выводилось из генератора ну и потом добавлять его в список вне генератора  - почему то получается пустой список
    # а если формировать список внутри функции как сделано здесь то все работает
    for item in data:
        if isinstance(item, list):
            foo(item)
        else:
            res.append(item)
    return res

if __name__ == '__main__':
    l = [[1, 2, 3, 4], [5, 6, 7],[8, 'ffkf']]
    print(list(FlatIterator(l)))
    # test_1()

    l = [[1, 2, 3, 4], [5, 6, 7], [8]]
    print(list(flat_generator(l)))
    test_2()

    l = [[[[[1, 2, [3, [4]], 'errrr']], [5, 6, 7]], 'wer', [8]]]
    print(foo(l))
