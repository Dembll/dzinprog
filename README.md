# Task 1
def before_after(func):
    def wrapper(*args, **kwargs):
        print("Перед виконанням функції")
        result = func(*args, **kwargs)
        print("Після виконання функції")
        return result
    return wrapper

@before_after
def my_function():
    print("Це функція!")

my_function()


# Task 2
def save_results_to_file(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'a') as file:
                file.write(f"Результат: {result}\n")
            return result
        return wrapper
    return decorator

@save_results_to_file('results.txt')
def multiply(a, b):
    return a * b

multiply(3, 5)
multiply(10, 2)


# Task 3
def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Виникла помилка: {e}")
            return None
    return wrapper

@handle_exceptions
def divide(a, b):
    return a / b

divide(5, 0)


# Task 4
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання: {end_time - start_time} секунд")
        return result
    return wrapper

@measure_time
def some_function():
    time.sleep(2)

some_function()


# Task 5
def log_arguments_results(func):
    def wrapper(*args, **kwargs):
        print(f"Аргументи: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

@log_arguments_results
def add_numbers(a, b):
    return a + b

add_numbers(3, 4)


# Task 6
def limit_calls(max_calls):
    def decorator(func):
        calls = 0
        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls < max_calls:
                calls += 1
                return func(*args, **kwargs)
            else:
                print("Перевищено ліміт викликів")
        return wrapper
    return decorator

@limit_calls(3)
def some_function():
    print("Виклик функції")

some_function()
some_function()
some_function()
some_function()


# Task 7
def cache_results(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            print("Використання кешу")
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

@cache_results
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Обчислюється
print(fibonacci(10))  # Використання кешу
