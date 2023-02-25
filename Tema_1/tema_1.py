# declară o listă care conține elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine).

list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# afișează lista inițială ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)

list_asc=list.copy()
list_asc.sort()
print("lista ordonata ascendent = ", list_asc)

# afișează lista inițială ordonată descendent (lista inițială trebuie păstrată în aceeași formă)

list_desc=list.copy()
list_desc.sort(reverse=True)
print("lista ordonata descendent = ", list_desc)

# afișează o listă ce conține numerele pare din lista ordonată (folosind slice)

list_desc= list_desc[0:9:2]
print("listă cu numerele pare = ", list_desc)

# afișează o listă ce conține numerele impare din lista ordonată (folosind slice)

list_asc= list_asc[0:9:2]
print("listă cu numerele impare = ", list_asc)

# afișează o listă ce conține numerele ce sunt multipli ai numărului 3 (folosind slice)

list_asc= list_asc[1:9:3]
print("listă cu multiplii de 3 = ", list_asc)

print("lista initiala = ", list)