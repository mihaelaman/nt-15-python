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

#scriem codul de mai sus in care utilizatorul introduce date de maxim 3 ori

for i in [1, 2, 3]:
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