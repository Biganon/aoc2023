import re

with open("input", "r") as f:
    lines = f.read().splitlines()

DIGITS = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
STIGID = tuple(digit[::-1] for digit in DIGITS)

total1 = total2 = 0

for line in lines:
    total1 += int("".join(re.sub(r"[^1-9]", "", line)[idx] for idx in (0, -1)))
    total2 += int("".join(re.sub(r"[^1-9]", "", re.sub(
        rf"({'|'.join(STIGID if inverted else DIGITS)})",
        lambda x: {digit: str(idx+1) for idx, digit in enumerate(STIGID if inverted else DIGITS)}[x.group(1)],
        line[::-1 if inverted else 1]
    ))[0] for inverted in (False, True)))

print(total1)
print(total2)
