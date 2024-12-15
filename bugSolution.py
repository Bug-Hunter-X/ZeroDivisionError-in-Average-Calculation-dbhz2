def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0  # Handle empty list case
    average = total / count
    return average

my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}")

my_list = [10,20,30,40,50]
average = calculate_average(my_list)
print(f"The average is: {average}") 