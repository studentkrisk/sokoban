# SPECIAL CHARS USED: ←,↑,→,↓
import sys

class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, b):
        return Vec2d(self.x + b.x, self.y + b.y)
    def __tuple__(self):
        return (self.x, self.y)
    def __repr__(self):
        return "{" + str(self.x) + ", " + str(self.y) + "}"
    def __eq__(self, o):
        return self.x == o.x and self.y == o.y
    def __hash__(self):
        return self.__repr__().__hash__()

class Block:
    def __init__(self, pos: Vec2d, v):
        self.pos = pos
        self.v = v
    def merge(self, o):
        if o.v.isnumeric() and self.v.isnumeric():
            self.v = str(int(o.v) + int(self.v))
        else:
            self.v = self.v + o.v
        self.pos = o.pos
    def __repr__(self):
        return (self.v if len(self.v) == 1 else "~") + ": " + str(self.pos)

class Map:
    def __init__(self, fg, bg, p):
        self.fg = fg
        self.bg = bg
        self.p = p
        self.out = ""

    # returns if its caller should move forward or not
    def move(self, b, d):
        infrontfg = self.getfg(b.pos + d)
        if infrontfg:
            if not self.move(infrontfg, d):
                b.merge(infrontfg)
                wrd.fg.remove(infrontfg)
                return True
        infrontbg = self.getbg(b.pos + d)
        if infrontbg and infrontbg.v == "#":
            return False
        b.pos += d
        under = self.getbg(b.pos)
        if under:
            match under.v:
                case "*":
                    self.out += b.v if not b.v.isnumeric() else chr(int(b.v))
                    self.fg.remove(b)
        return True
    
    def get(self, pos):
        fg = self.getfg(pos)
        bg = self.getbg(pos)
        if fg:
            return fg
        if bg:
            return bg
        return None
    
    def getfg(self, pos):
        for i in self.fg:
            if i.pos == pos:
                return i
        return None
    def getbg(self, pos):
        for i in self.bg:
            if i.pos == pos:
                return i
        return None
    
    def __repr__(self):
        out = ""
        for y in range(1+max(map(lambda y : y.pos.y, fg + bg))):
            for x in range(1+max(map(lambda y : y.pos.x, fg + bg))):
                pos = Vec2d(x, y)
                to_print = self.get(pos)
                if pos == self.p.pos:
                    to_print = self.p
                out += (to_print.v if len(to_print.v) == 1 else "~") if to_print else " "
            out += "\n"
        return out
        

bg = []
fg = []
with open("helloworld.skbn", "r") as f:
    m = list(map(list, f.read().split("\n")))
    size = Vec2d(len(m[0]), len(m))
    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] != " ":
                if ord("a") <= ord(m[y][x]) <= ord("z") or ord("A") <= ord(m[y][x]) <= ord("Z") or ord("0") <= ord(m[y][x]) <= ord("9"):
                    fg.append(Block(Vec2d(x, y), m[y][x]))
                else:
                    bg.append(Block(Vec2d(x, y), m[y][x]))
d = Vec2d(0, 0)
wrd = Map(fg, bg, Block(Vec2d(0, 0), "@"))

while True:
    print(wrd)
    wrd.move(wrd.p, d)
    input(wrd)
    if not wrd.getbg(wrd.p.pos):
        continue
    match wrd.getbg(wrd.p.pos).v:
        case "→":
            d = Vec2d(1, 0)
        case "←":
            d = Vec2d(-1, 0)
        case "↓":
            d = Vec2d(0, 1)
        case "↑":
            d = Vec2d(0, -1)
        case ".":
            break
print(wrd.out)