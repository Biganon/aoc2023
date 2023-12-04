with open("input", "r") as f:
    lines = f.read().splitlines()

total = 0

copies = {k: 1 for k in range(1, len(lines)+1)}

for line in lines:
    iden, values = line.split(":")
    iden = int(iden.split(" ")[-1])
    todo = copies[iden]
    winning, present = map(lambda x: set(y for y in x.split(" ") if y), values.split("|"))
    nb = len(winning.intersection(present))
    score = 0 if nb == 0 else 2 ** (nb - 1)
    total += score
    for i in range(todo):
        for j in range(nb):
            copies[iden+j+1] += 1

print(total)
print(sum(copies.values()))
