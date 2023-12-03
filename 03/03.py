from collections import defaultdict

with open("input", "r") as f:
    lines = f.read().splitlines()

gears = defaultdict(set)
numbers = {}

total1 = total2 = 0

for y, line in enumerate(lines):
    number = ""
    for x, char in enumerate(line):
        if char.isdigit():
            number += char

        if (not char.isdigit()) or x == (len(line) - 1):
            if char.isdigit():
                x += 1
            if number:
                a = x - len(number)
                z = x - 1
                n_ok = y > 0
                w_ok = a > 0
                e_ok = z < (len(line) - 1)
                s_ok = y < (len(lines) - 1)
                n = lines[y-1][a:z+1] if n_ok else "."
                w = lines[y][a-1] if w_ok else "."
                e = lines[y][z+1] if e_ok else "."
                s = lines[y+1][a:z+1] if s_ok else "."
                nw = lines[y-1][a-1] if n_ok and w_ok else "."
                ne = lines[y-1][z+1] if n_ok and e_ok else "."
                sw = lines[y+1][a-1] if s_ok and w_ok else "."
                se = lines[y+1][z+1] if s_ok and e_ok else "."
                if any(c for c in n + w + e + s + nw + ne + sw + se if c != "." and not c.isdigit()):
                    total1 += int(number)
                for i, c in enumerate(nw + n + ne):
                    if c == "*":
                        gears[(y-1, a-1+i)].add((y, a))
                if w == "*":
                    gears[(y, a-1)].add((y, a))
                if e == "*":
                    gears[(y, z+1)].add((y, a))
                for i, c in enumerate(sw + s + se):
                    if c == "*":
                        gears[(y+1, a-1+i)].add((y, a))
                numbers[(y, a)] = int(number)
            number = ""

print(total1)

gears = [gear for gear in gears.items() if len(gear[1]) == 2]
for gear in gears:
    value = list(gear[1])
    number1 = numbers[value[0]]
    number2 = numbers[value[1]]
    total2 += number1 * number2

print(total2)
