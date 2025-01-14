plik = open("napisy.txt", "r")

#4.1
w = 0
for linijka in plik:
    for znak in linijka:
        if ord(znak) >= 48 and ord(znak) <= 58:
           w = w+1
print(w)

#4.2