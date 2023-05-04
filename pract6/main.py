from lst import create_node, hasNext, iter_lst


## 2.2
# Создайте функцию make_list(*args), 
# которая создает список на основе аргументов.

def make_list(*args):
    node = None
    for val in args[::-1]:
        node = create_node(val, node)
    return node

lst = make_list(0,1,2,3,4,5,6)

## 2.3
# Создайте функцию list_to_string(lst), 
# возвращающую строку, содержащую элементы списка.

def list_to_string(lst) -> str:
    string = '[ '

    iter = iter_lst(lst)
    try: 
        while True:
            val=next(iter)
            string+=str(val)+' '
    except:
        pass

    string+=']'
    return string

def print_lst(lst):
    print(list_to_string(lst))

# print(list_to_string(lst))


## 2.4
# Создайте функцию list_range(low, high), 
# возвращающую список чисел 
# от low до high включительно.

def list_range(low: int, high: int):
    node = None
    for val in range(high, low-1, -1):
        node = create_node(val, node)
    return node

# print_lst(list_range(1,10))

## 2.5
# Создайте функцию foldl(func, lst, acc),
# вычисляющую свертку элементов списка, аналогично reduce

def foldl(func, lst, acc=None):

    it = iter_lst(lst)

    value = None
    try: 
        if acc is None:
            value = next(it)
        else:
            value = acc

        while True:
            value = func(value, next(it))
    except:
        pass

    return value

# print(foldl(lambda x,y: x+y,lst,10))


# 2.6
# Создайте функцию list_sum(lst) для вычисления суммы 
# элементов списка с помощью foldl.

def list_sum(lst):
    return foldl(lambda res,x: res+x, lst)

# print(list_sum(lst))


# 2.7
# Создайте функцию fact(n) для вычисления 
# факториала с помощью foldl и list_range.

def fact(n):
    if n<0:
        raise Exception("Аргумент должен быть больше нуля")

    if n==0:
        return 1

    lst = list_range(1, n)
    return foldl(lambda res,x: res*x, lst)

# print(fact(4))


# 2.8 
# Создайте функцию list_to_py(lst) для 
# преобразования списка 
# в обычный список Питона с помощью foldl.

def list_to_py(lst):
    return foldl(lambda res,x: [*res, x], lst, [])

# lst = list_range(0, 1)
# print(list_to_py(lst))

# 2.9
# Создайте функцию list_reverse(lst) для разворота 
# списка в обратном направлении с помощью foldl.

lst = list_range(0, 10)
print_lst(lst)
def list_reverse(lst):
    val, nodeNext = lst()
    firstNode = create_node(val, None)

    return foldl(lambda res,x: create_node(x, res), nodeNext,firstNode)

print_lst(list_reverse(lst))