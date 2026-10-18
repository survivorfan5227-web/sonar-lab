def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot average an empty list")
    return sum(numbers) / len(numbers)


def multiply(a, b):
    return a * b


def main():
    nums = [4, 8, 15, 16, 23, 42]
    print("Average:", calculate_average(nums))
    print("Division:", divide(10, 2))
    print("Multiplication:", multiply(4, 5))


if __name__ == "__main__":
    main()

