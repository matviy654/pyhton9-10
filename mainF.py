#task1
# def product_of_list(numbers):
#     product = 1
#     for number in numbers:
#         product *= number
#     return product

# example_list = [1, 2, 3, 4, 9]
# result = product_of_list(example_list)
# print(f"Добуток елементів списку: {result}")

#task2
# def find_minimum(numbers):
#     if not numbers:
#         raise ValueError("Список не може бути порожнім")

#     minimum = numbers[0]
#     for number in numbers:
#         if number < minimum:
#             minimum = number
#     return minimum

# example_list = [5, 59, 9, 59, 5, 6]
# result = find_minimum(example_list)
# print(f"Мінімальне значення у списку: {result}")

#task3
# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

# def count_primes(numbers):
#     prime_count = 0
#     for number in numbers:
#         if is_prime(number):
#             prime_count += 1
#     return prime_count

# example_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# result = count_primes(example_list)
# print(f"Кількість простих чисел у списку: {result}")

#task4
# def elements(nums, val):
#     count = 0
#     i = 0
#     while i < len(nums):
#         if nums[i] == val:
#             nums.pop(i)
#             count += 1
#         else:
#             i += 1
#     return count

# nums = [3, 2, 9, 3, 0, 5, 3]
# val = 3
# deleted_count = elements(nums, val)
# print("Кількість видалених елементів:", deleted_count)
# print("Список після видалення:", nums)

#task5
# def merge_lists(list1, list2):
#     merged_list = list1 + list2
#     return merged_list

# list1 = [9, 5, 1]
# list2 = [4, 5, 3]
# result = merge_lists(list1, list2)
# print("Об'єднаний список:", result)

#task6
# def calculate_powers(nums, power):
#     powered_list = []
#     for num in nums:
#         powered_list.append(num ** power)
#     return powered_list

# numbers = [1, 2, 3, 84, 5]
# degree = 3
# powered_numbers = calculate_powers(numbers, degree)
# print("Список чисел піднесений до ступеня {}: {}".format(degree, powered_numbers))


