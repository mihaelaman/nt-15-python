#a = 15 # a=15 si b=3 => a+b=153
#b = int(a)
#c = 3

#print(a)

#user_input = input("insert a number: ") # user_input este string (sirul de caractere de la tastatura)
# user_input = int(user_input) # user_input devine un numar, atunci trebuie sa introducem un nr, string da eroare
# print('user_input = ', user_input)

#user_input = input("insert a number: ")

#try:
#    user_input = int(user_input)
#except ValueError as e: #exceptia de tip value error o sa fie tratata ca si e, eroarea generata de cod
#    print(e)
#    print(f"You inserted '{user_input}' which is not a valid number!")

#print("Valid instruction.")

# cum pot trata mai multe exceptii? de ex: Name Error

#try:
#    user_input = int(user_input)
#    print(undefined_variable)
#except Exception as e: # exception sunt toate eroriile
#    print("I caught the following exception: ", e, type(e))
#
# print("Valid instruction.")

# user_name = input("Name: ")
# print("Name: ", user_name)
#
# user_age = input("Age: ")
# try:
#     print("Age: ", user_age)
# except ValueError:
#     print("Age", user_age, "(this is invalid value)")
#
# print("City: ", user_city)
# user_city = input("City: ")

#exista erori de programare si erori de user - pt erorile de user se foloseste try-except
#else if = elif

# user_age = input("age: ")
# try:
#     user_age = int(user_age)
#
#     if user_age > 18:
#         print("you're a grown up")
# except ValueError:
#     print("invalid age")

# user_age = input("age: ")
# try:
#     user_age = int(user_age)
#
# except ValueError:
#     print("invalid age")
#
# if type(user_age) == int and user_age >= 18:
#     #            True     and     True      =>  True
#          print("you're a grown up")

#user_age = input("age: ")

# try:
#     user_age = int(user_age)
#
# except ValueError:
#     print("invalid age")
#
# if user_age >= 18:
#     print("you're a grown up")
# else:
#     print("you're a child")

# try:
#     user_age = int(user_age)
#
# except ValueError:
#     print("invalid age")
# else: #ramura de else al try, care se executa doar in caz ca celalalte se ruleaza ok
#
#     if user_age >= 18:
#         print("you're a grown up")
#     else:
#         print("you're a child")

# try:
#     user_age = int(user_age)
#
# except ValueError:
#     print("invalid age")
# else:
#
#     if user_age >= 18:
#         print("you're a grown up")
#     else:
#         print("you're a child")
# finally:
#     print("end of the program") #se ruleaza chiar daca avem exceptia din ramura de try

#user_age = int(input("age: "))
#<18 -> child
#<14 -> without id
#>=18 -> adult
#>=65 -> retired

# if user_age >= 18:
#     print("you're a grown up")
#
#     if user_age >= 65:
#         print("you're a retired person")
# else:
#     print("you're a child")
#
#     if user_age < 14:
#         print("you don't have an ID")

# if user_age < 14:
#     print("you don't have an ID")
# elif user_age < 18:
#     print("you're a child")
# elif user_age > 18:
#     print("you're an adult")
# else:
#     print("you're a retired person")

# while True:
#     print("inside while loop")

# my_numbers = [54, 23, 78, -2] # len(my_numbers) = 4
#
# for item in my_numbers:
#     print(item)
# valabil pt liste, tupluri si seturi (in set nu o sa se pastreze neaparat ordinea)

# my_numbers = [54, 23, 78, -2] # len(my_numbers) = 4

# for item in my_numbers:
#     print(f"item with value = {item} is on index = {my_numbers.index(item)}")

#print(list(enumerate(my_numbers))) # o lista de tupluri in care avem elem si indexul elem

# for element in enumerate(my_numbers):
#     print(f"item with value = {element[1]} is on index = {element[0]}")

# my_tuple = (56, -2, 14)
# a, b, c = my_tuple # in a se pune valoare elem 1 din tuplu samd
# print(a)
# print(b)
# print(c) #se foloseste pt tupluri

# my_numbers = [54, 78, 23, -2]
# for index, element in enumerate (my_numbers):
#     print(f"item with value = {element} is on index = {index}")

# my_numbers = [54, 78, 23, -2]
# for index, element in enumerate (my_numbers):
#     print(f"item with value = {element} is on index = {index}")

# my_numbers = [12, 56, -2, 14]
# index = 0
# while index < len(my_numbers):
#     print(f"item with value = {my_numbers[index]} is on index = {index}")
#     index = index + 1

# for number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     if number % 2 == 0:
#         print(f"number = {number}")
#         continue # trece la urmatoarea iteratie, BREAK ne scoate din bucla
#
#     print("print whatever number you are dealing with")

#for number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#    pass # ca sa poti sa ai un cod valid, rol de placeholder, pana revii la instructiune

