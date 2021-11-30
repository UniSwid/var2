import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print('затрачено времени', time.perf_counter() - start)
        return result
    return wrapper


# 1 упражнение
@timer
def f(n, s):
    print('была вызвана функция def f')
    from math import pi, tan
    return (n * s ** 2) / (4 * tan(pi / n))


S = f(int(input()), float(input()))
print('ответ', S)


# 2 упражнение
@timer
def g(n):
    print('была вызвана функция def g')
    return (n * (n + 1)) / 2


C = g(int(input()))
print('ответ', C)