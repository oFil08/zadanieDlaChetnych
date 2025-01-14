def isPali(s):
    return s == s[::-1]

# 4.1
with open("napisy.txt", "r") as file:
    w = 0
    for line in file:
        w += sum(1 for char in line if '0' <= char <= '9')
    print(w)

# 4.2
with open("napisy.txt", "r") as file:
    answ1 = []
    i1 = 0
    i2 = 0
    for line in file:
        line = line.strip()
        i1 += 1
        if i1 % 20 == 0:
            if i2 < len(line):
                answ1.append(line[i2])
                i2 += 1
    print("".join(answ1))

# 4.3
with open("napisy.txt", "r") as file:
    answ2 = []
    for line in file:
        line = line.strip()
        if isPali(line + line[0]):
            answ2.append(line[25])
        elif isPali(line[49] + line):
            answ2.append(line[24])
    print("".join(answ2))

# 4.4
with open("napisy.txt", "r") as file:
    result = []
    stop_counter = 0

    for line in file:
        digits = "".join(char for char in line if '0' <= char <= '9')
        digits = digits[:len(digits) - len(digits) % 2]

        for i in range(0, len(digits), 2):
            num = int(digits[i:i + 2])
            if 65 <= num <= 90:
                char = chr(num)
                result.append(char)
                stop_counter = stop_counter + 1 if char == 'X' else 0
                if stop_counter == 3:
                    print("".join(result))
                    exit()

    print("".join(result))

