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

# for i in range(3):
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

# Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor
# care reprezintă numere întregi sau reale.
#       your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3).
#       your_function() va returna 0.
#       your_function(2, 4, ‘abc’, param_1=2) va returna 6 (2 + 4).


def your_function(*args, **kwargs):
    sum = 0

    if len(args) == 0 and len(kwargs) == 0:
        return 0

    for arg in args:
        if isinstance(arg, (int, float)):
            sum = sum + arg

    if kwargs:
        for kwarg in kwargs:
            if isinstance(kwarg, (int, float)):
                sum = sum + kwarg

    return str(sum)


your_function()
print(your_function())
a = your_function(1, 5, -3, 'abc', [12, 56, 'cad'])
print(a)
a = your_function(2, 4, 'abc', param_1=2)
print(a)


# Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:
#   suma tuturor numerelor de la [0, n]
#   suma numerelor pare de la [0, n]
#   suma numerelor impare de la [0, n]


def suma(n):
    if n == 0:
        return 0, 0, 0
    else:
        sum_par, suma_total, sum_impar = suma(n - 1)
        suma_total += n
        if n % 2 == 0:
            sum_par += n
        else:
            sum_impar += n
    return suma_total, sum_par, sum_impar


print(suma(3))


# Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg,
# altfel returnează valoarea 0

def verify_int():
    try:
        a = int(input('number: '))
        return a
    except ValueError:
        return 0


print(verify_int())
