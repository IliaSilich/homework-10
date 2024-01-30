from typing import List
import time


def benchmark(func):
    def wrapper(seq: List[int]) -> List[int]:
        start = time.perf_counter()
        result = func(seq)
        end = time.perf_counter()
        elapsed_time = end - start
        print(f"Время выполнения: {elapsed_time:.40f} секунд")
        return result
    return wrapper


def slicer(func):
    def wrapper(seq: List[int]) -> List[int]:
        result = []
        for i in range(0, len(seq), 10):
            sublist = seq[i:i + 10]
            result.extend(func(sublist))
        return result
    return wrapper


@slicer
@benchmark
def func2(seq: List[int]) -> List[int]:
    if len(seq) > 10:
        raise ValueError("Превышено максимальное количество элементов (больше 10)")

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    new_seq = [factorial(num) for num in seq]
    return new_seq


def func1() -> int:
    input_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    result_sum = sum(func2(input_sequence))
    return result_sum


print(func1())
