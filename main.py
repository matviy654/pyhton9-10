#task1
# def printsms():
#     sms = """\
# "Don't compare yourself with anyone in this world…
# if you do so, you are insulting yourself."
# Bill Gates"""
#     print(sms)

# printsms()

#task2
# def even_numbers(start, end):
#     if start > end:
#         start, end = end, start 
    
#     for i in range(start, end + 1):
#         if i % 2 == 0:
#             print(i)

# even_numbers(4, 30)

#task3
# def printsquare(side_length, symbol, filled):
#     for i in range(side_length):
#         if filled or i == 0 or i == side_length - 1:
#             print(symbol * side_length)
#         else:

#             print(symbol + ' ' * (side_length - 2) + symbol)


# printsquare(5, '*', True)
# print()  
# printsquare(5, '*', False)

#task4
# def find_minimum(a, b, c, d, e):
#     return min(a, b, c, d, e)

# minimum = find_minimum(8, 5, 8, 7, 120)
# print(f"Мінімальне значення: {minimum}")

#task5
# def product_in_range(start, end):
#     if start > end:
#         start, end = end, start  
    
#     product = 1
#     for number in range(start, end + 1):
#         product *= number
        
#     return product

# result = product_in_range(5, 6)
# print(f"Добуток чисел у діапазоні: {result}")

#task6
# def count_digits(number):
#     return len(str(abs(number)))


# digit_count = count_digits(39756)
# print(f"Кількість цифр у числі: {digit_count}")

#task7
# def is_palindrome(number):
#     str_number = str(number)
#     return str_number == str_number[::-1]
# print(is_palindrome(123321))  
# print(is_palindrome(546845))  
# print(is_palindrome(421987))  
