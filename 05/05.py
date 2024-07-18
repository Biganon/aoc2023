with open("input", "r") as f:
    lines = f.read().splitlines()

tables = []

for line in lines:
    if "seeds" in line:
        seeds = map(int, (x for x in line.split(":")[1].split(" ") if x))
        continue

    if "map" in line:
        tables.append([])
        continue

    if not line:
        continue

    tables[-1].append(list(map(int, line.split(" "))))

matchings = {}

for seed in seeds:
    current = seed
    for idx, table in enumerate(tables):
        for conversion in table:
            d_start, s_start, length = conversion
            if s_start <= current <= (s_start + length - 1):
                delta = current - s_start
                current = d_start + delta
                break
    matchings[seed] = current

print(min(matchings.values()))