"""
Bonus Problem: Introduction to Recursion
Learn about recursive functions - functions that call themselves!
"""


def factorial(n):
    """
    Calculate factorial of n using recursion.
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def countdown(n):
    """
    Print numbers from n down to 1 using recursion.
    """
    if n == 0:
        print("Blastoff!")
        return
    print(n)
    countdown(n - 1)


def sum_list(numbers):
    """
    Calculate sum of list using recursion.
    """
    if not numbers:
        return 0
    return numbers[0] + sum_list(numbers[1:])


def fibonacci(n):
    """
    Calculate nth Fibonacci number using recursion.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def power(base, exponent):
    """
    Calculate base^exponent using recursion.
    """
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


def reverse_string(text):
    """
    Reverse a string using recursion.
    """
    if len(text) <= 1:
        return text
    return text[-1] + reverse_string(text[:-1])


def count_down_list(n):
    """
    Create a list of numbers from n down to 1 using recursion.
    """
    if n == 0:
        return []
    return [n] + count_down_list(n - 1)


def flatten_list(nested_list):
    """
    Flatten a nested list using recursion.
    """
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


# Test cases
if __name__ == "__main__":
    print("Testing Recursive Functions...")
    print("-" * 50)

    print("Test 1: factorial")
    assert factorial(5) == 120
    assert factorial(0) == 1
    print("✓ Passed\n")

    print("Test 2: countdown")
    countdown(5)
    print("✓ Passed\n")

    print("Test 3: sum_list")
    assert sum_list([1, 2, 3, 4, 5]) == 15
    assert sum_list([]) == 0
    print("✓ Passed\n")

    print("Test 4: fibonacci")
    fib_sequence = [fibonacci(i) for i in range(7)]
    assert fib_sequence == [0, 1, 1, 2, 3, 5, 8]
    print("✓ Passed\n")

    print("Test 5: power")
    assert power(2, 5) == 32
    assert power(3, 3) == 27
    assert power(10, 0) == 1
    print("✓ Passed\n")

    print("Test 6: reverse_string")
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"
    print("✓ Passed\n")

    print("Test 7: count_down_list")
    assert count_down_list(5) == [5, 4, 3, 2, 1]
    print("✓ Passed\n")

    print("Test 8: flatten_list")
    nested = [1, [2, 3], [4, [5, 6]], 7]
    assert flatten_list(nested) == [1, 2, 3, 4, 5, 6, 7]
    print("✓ Passed\n")

    print("=" * 50)
    print("All recursion tests passed!")