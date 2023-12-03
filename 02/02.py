with open("input", "r") as f:
    lines = f.read().splitlines()

total1 = total2 = 0
red_content = 12
green_content = 13
blue_content = 14

for line in lines:
    title, game = line.split(":")
    iden = int(title.split(" ")[1])
    subsets = game.split(";")
    max_r = 0
    max_g = 0
    max_b = 0
    too_many = False
    for subset in subsets:
        colors = subset.split(",")
        red = int(red[0].split(" ")[1]) if (red := [x for x in colors if "red" in x]) else 0
        green = int(green[0].split(" ")[1]) if (green := [x for x in colors if "green" in x]) else 0
        blue = int(blue[0].split(" ")[1]) if (blue := [x for x in colors if "blue" in x]) else 0
        if red > red_content or green > green_content or blue > blue_content:
            too_many = True
        max_r = max(max_r, red)
        max_g = max(max_g, green)
        max_b = max(max_b, blue)
    if not too_many:
        total1 += iden
    power = max_r * max_g * max_b
    total2 += power

print(total1)
print(total2)
