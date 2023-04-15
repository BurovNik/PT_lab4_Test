# part 1
# task 6 +
def fibonacci(n: int) -> int:
    if n < 0:
        print('Wrong number')
        return 0
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(-7))
print(fibonacci(7))


# task 12 +

# we had to change the function to be able to test. The function now returns a bool value
def check_pow2(number: int, check_value=1) -> bool:
    if number == 1:
        print('YES')
        return True
    elif number % 2 == 1:
        print('NO')
        return False
    else:
        return check_pow2(number // 2, check_value)


check_pow2(12)

# task 13 +


def negative_sum(lst: list[int]) -> int:
    if len(lst) == 0:
        return 0
    elif lst[0] < 0:
        return lst[0] + negative_sum(lst[1:])
    else:
        return negative_sum(lst[1:])


test_list = [-1, 2, 3, -2, -34, -2, 11, -56]
print(negative_sum(test_list))


# task 14 +

def recursion_pow(x: int, y: int) -> int:
    if y == 0:
        return 1
    elif y < 0:
        print('Wrong pow')
        return 0
    else:
        return x * recursion_pow(x, y - 1)


print(recursion_pow(2, 4))
print(recursion_pow(5, 2))
print(recursion_pow(-3, 3))
print(recursion_pow(2, -2))

# part 2
# task 5 +


def closure_comparison(r: str):
    def inner_fun(x: float, y: float) -> bool:
        if r == '>':
            return x > y
        elif r == '<':
            return x < y
        elif r == '=':
            return x == y
        else:
            return False
    return inner_fun


a = closure_comparison('<')
print(a(3, 5))


# task 6 +


def closure_del_str(my_str: str):
    def closure_del_str_inner(symbol: str) -> str:
        new_str = my_str.replace(symbol, '')
        return new_str
    return closure_del_str_inner


test_str = closure_del_str('Test string')
print(test_str('s'))
test_str = closure_del_str('Test string')
print(test_str('t'))


# task 9


def closure_list_pow(lst: list):
    def closure_list_pow_inner(my_pow: int) -> list:
        nonlocal lst
        lst = [it ** my_pow for it in lst]
        return lst
    return closure_list_pow_inner


a = closure_list_pow([1, 2, 3, 4])
print(a(3))
