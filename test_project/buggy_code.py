def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]

    return total / len(numbers)


nums = [10, 20, 30, 40]
print("Average is:", calculate_average(nums))


# Bug: division by zero case not handled
print("Average empty:", calculate_average([]))