# def my_first_function():
#     print("hello from my first function!")
#
# my_first_function()

# def show_sum_of_numbers():
#     a = int(input("a="))
#     b = int(input("b="))
#     print(f"sum of {a} and {b} is {a + b}")
#
# show_sum_of_numbers()

# def show_sum_of_numbers():
#     while True:
#         Try:
#             a = int(input("a="))
#         except ValueError:
#             print("value of a is not a number. Try again")
#
#     while True:
#         Try:
#             b = int(input("b="))
#         except ValueError:
#             print("value of a is not a number. Try again")
#
#     print(f"sum of {a} and {b} is {a + b}")

# show_sum_of_numbers()

# def get_number():
#     number = int(input("number:"))
#     print("number", number)
#     return number  # o fct daca nu are return o sa afiseze by default NONE
#
# a = get_number()
# b = get_number()
# print("sum = ", a + b)

# def get_number():
#     number = int(input("number:"))
#     print("number", number)
#     return number  # o fct daca nu are return o sa afiseze by default NONE
#
# def show_of_numbers():
#     a = get_number()
#     b = get_number()
#     print("first number is:", a)
#     print("second number is:", b)
#     print("sum = ", a + b)

# def get_number():
#     number = int(input("number: "))
#     return number
#
#
# def get_validated_number():
#     while True:
#         try:
#             number = get_number()
#             return number
#         except ValueError:
#             print("value is not a number. Try again")
#
#
# def show_sum_of_numbers(a, b):
#     # a = get_validated_number()
#     # b = get_validated_number()
#
#     print(f"sum of {a} and {b} is {a + b}")
#
#
# n1 = get_validated_number()
# n2 = get_validated_number()
# show_sum_of_numbers(n1, n2)


# def my_function(my_list):
#     my_list.append(4)
#
#
# l1 = [1, 2, 3]
# print("1.", l1)
# my_function(l1) # ii tirmitem locatia de memorie l1
# print("2.", l1)


# def my_function(my_list):
#     my_list.append(4)
#     return my_list
#
#
# l1 = [1, 2, 3]
# l2 = my_function(l1)
# print("1.", l1)
# print("2.", l2)
# print("3.", l1 == l2)
# print("4.", l1 is l2)


# def my_function(my_list):
#     my_list = list(my_list) # my_list.copy(); my_list[:] - metode de a copia o lista
#     my_list.append(4)
#     return my_list
#
#
# l1 = [1, 2, 3]
# l2 = my_function(l1)
#
# assert l1 is l2 #aceasta fct da eroare daca rasp este FALSE si nu da nimic daca e TRUE
# assert l1 != l2


# def sort(my_list):
#     pass
#
#
# numbers = [1, 6, 2, 8, 3]
# sort(numbers)


# def f(param_1, param_2, param_3="abc"):
#     print(param_1, param_2, param_3)
#
#
# f("a","b")
# f("a","b", param_3="def")


# def do_math(a, b, operation="*"):
#     if operation == "*":
#         return a * b
#     if operation == "/":
#         return a / b
#     if operation == "-":
#         return a - b
#     return a + b
#
#
# print(do_math(2, 7))
# print(do_math(2, 7, operation="*"))


# VARIABLE LENGTH ARGUMENTS: parametrii ce treb definit cu *
# def f(*args):
#     print(args)
#
# f()
# f(10,2,3)


# def f(*args, **kwargs):
#     print(args, kwargs)


# def f(a, b):
#     return a + b


# a = f
# print(a(2, 7))


# def g(my_function):
#     return my_function(2, 7)
#
# print(g(f))


# def g():
#     def f(a, b)
#         return a + b
#
#     return f
#
#
# a = g()
# print(a(2, 7))


# def f1():
#     print("my var value in f1", my_variable)
#
#
# f1()
# print("my var value in main program", my_variable)


# print all number from 0 to n
# def f(n):
#
#     if n > 0:
#         f(n-1)
#
#     print(n)
#
# f(5)


# def f(n):
#     # if n > 0:
#     #     previous_step_list = f(n - 1)
#     #     print(previous_step_list)
#     #
#     # return [n]
#     if n == 0:
#         return [0]
#     previous_step_list = f(n - 1)
#     previous_step_list.append(n)
#
#     return previous_step_list
#
#
# l = f(5)
# print(l)

# TYPE ANNOTATIONS / TYPE HINTS

# def f(a: int, b: int):  # pt a ne asteptam sa fie integer
#     print(a + b)
#
#
# f(2, 5)


def f(n: int):
    return list(range(n))


result = f(5)
