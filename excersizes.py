l1 = [1,2,3,4,5,6,7,]
l2 = [1,3,5,]

def compare_lists(l1:list, l2:list) -> list:
    return set(l1) - set(l2)

# когда речь идет о сравнении множеств, наиболее эффективный инструмент это set.
# Они реализованы как хэш таблицы, поэтому работают очень быстро.
# Но тут следует иметь в виду, что мы потеряем дублирующиеся элементы,
# поэтому решение не всегда годится.

print(compare_lists(l1, l2))

l3 = [1,0,2,0,3]
def remove_zeroes(l: list) -> list:
    return [i for i in l if i != 0]

print(remove_zeroes(l3))

# List comprehetion - очень быстрая конструкция языка, более эффективная чем for.
# Она очень экономична к памяти.
