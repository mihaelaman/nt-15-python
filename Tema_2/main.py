# while True:
#     try:
#         age = int(input('Age: '))
#     except ValueError:
#         print("Invalid valid. Try again.")
#         continue
#
#     if age >= 18:
#         print("You are a grown up!")
#     else:
#         print("You are a child!")
#
#     break

# scriem codul de mai sus in care utilizatorul introduce date de maxim 3 ori

for i in range(3):
    try:
        age = int(input('Age: '))
    except ValueError:
        print("Invalid valid. Try again.")
        continue

    if age >= 18:
        print("You are a grown up!")
    else:
        print("You are a child!")

    break

# Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor
# care reprezintă numere întregi sau reale.
#       your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3).
#       your_function() va returna 0.
#       your_function(2, 4, ‘abc’, param_1=2) va returna 6 (2 + 4).


def your_function(*args):

        sum = 0
        operations = ""

        if len(args) == 0:
            return 0

        for arg in args:
            if isinstance(arg, (int, float)):
                sum = sum + arg
                if arg < 0:
                    operations = operations + str(arg)
                else:
                    operations = operations + "+" + str(arg)
        operations = operations[1:]
        return str(sum) + f" ({operations})"

your_function()
print(your_function())
a = your_function(1, 5, -3, 'abc', [12, 56, 'cad'])
print(a)
# a = your_function(2, 4, 'abc', param_1=2)
# print(a)

# Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:
#   suma tuturor numerelor de la [0, n]


def sum_total (n):
    if n==0:
        return 0
    else:
        return n + sum_total(n-1)

print("sum = ", sum_total(9))


#   suma numerelor pare de la [0, n]
def sum_par (n):
    if n == 0:
        return 0
    if n%2==0:
        return n + sum_par(n-1)
    else:
        return sum_par(n-1)


print("sum = ", sum_par(4))

#   suma numerelor impare de la [0, n]
def sum_impar (n):
    if n == 0:
        return 0
    if n%2==0:
        return sum_impar(n-1)
    else:
        return n + sum_impar(n-1)


print("sum = ", sum_impar(8))

#Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg,
# altfel returnează valoarea 0

def verify_int():
    try:
        a = int(input('number: '))
        return a
    except ValueError:
        return 0
print(verify_int())