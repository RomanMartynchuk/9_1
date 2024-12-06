def apply_all_func(int_list, *functions):
    results = {}
    try:
        for i in functions:
            if i == max:
                result = {}
                result[i.__name__] = max(int_list)
                results.update(result)
            if i == min:
                result = {}
                result[i.__name__] = min(int_list)
                results.update(result)
            if i == len:
                result = {}
                result[i.__name__] = len(int_list)
                results.update(result)
            if i == sum:
                result = {}
                result[i.__name__] = sum(int_list)
                results.update(result)
            if i == sorted:
                result = {}
                result[i.__name__] = sorted(int_list)
                results.update(result)
        return results
    except TypeError:
        return 'Используйте списки чисел'

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
# проверка всех функций с int, float
print(apply_all_func([6, 20, 15, 9.99], max, min, len, sum, sorted))
# отработка в случае передачи некорректных данных str
print((apply_all_func(["6, 20, 15, 9.99"], max, min, len, sum, sorted)))