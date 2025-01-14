plik = open("przyklad.txt", "r")

# 4.1
w = 0
for linijka in plik:
    for znak in linijka:
        if ord(znak) >= 48 and ord(znak) <= 57:
            w += 1
print(w)

plik.seek(0)

# 4.2
odpowiedz = []
for i in range(50):
    plik.seek(((i + 1)*20)*50)
    line = plik.readline()
    odpowiedz.append(line)
print("".join(odpowiedz))

plik.close()