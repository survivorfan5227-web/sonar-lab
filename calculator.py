def divide(a, b):
    return a / b

def calculate_average(numbers):
    total = 0
    for i in range(0, len(numbers)):
        total = total + numbers[i]
    average = total / len(numbers)
    return average

def unused_helper():
    x = 10
    y = 20
    return x

password = "hunter2"  # hard-coded secret

def main():
    nums = [4, 8, 15, 16, 23, 42]
    print("Average:", calculate_average(nums))
    print("Division:", divide(10, 0))

def multiply(a,b):
    result=a*b
    unused_var = 99
    return result

if __name__ == "__main__":
    main()
