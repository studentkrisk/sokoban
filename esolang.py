def printmap(bg, fg, p):
    for y in range(len(bg)):
        for x in range(len(bg[y])):
            print((fg[y][x] if fg[y][x] != " " else bg[y][x]) if [y, x] != p else "@", end="")
        print("")
    print("")

def move()

bg = []
fg = []
with open("test.skbn", "r") as f:
    m = list(map(list, f.read().split("\n")))
    bg = list(map(lambda x : list(map(lambda y : y if y in ".v<^>" else " ", x)), m))
    fg = list(map(lambda x : list(map(lambda y : y if y not in ".v<^>" else " ", x)), m))
print(bg)

p = [0, 0]
d = [0, 0]
c = " "

while True:
    move(m, p, d)
    c = bg[p[0]][p[1]]

    printmap(bg, fg, p)
    match c:
        case ">":
            d = [0, 1]
        case "<":
            d = [0, -1]
        case "v":
            d = [1, 0]
        case "^":
            d = [-1, 0]
        case ".":
            break