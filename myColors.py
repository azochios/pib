ESC = '\x1b'
RESET = ESC + '[0m'

COLORS = {
    1 : ["[30m", "paint it black"],
    2 : ["[34m", "insidious blue"],
    3 : ["[32m", "fiery green"],
    4 : ["[36m", "vicious cyan"],
    5 : ["[31m", "redemption dead red"],
    6 : ["[35m", "deep purple"],
    7 : ["[33m", "clockwork orange"],
    8 : ["[37m", "fluffy white"]
}

DEFAULT = "paint it black"

def printColors():
    for k, v in COLORS.items():
        print(f"{k}) {ESC}{v[0]}{v[1]}{RESET}")

def pickColor(question):
    txt = f"Please choose a color (1-8) for {question}:"
    print(txt)
    printColors()

    valid = False
    while not valid:
        try:
            choice = int(input())
            assert choice > 0 and choice <= len(COLORS)
            valid = True
        except (AssertionError, ValueError):
            print("Please stop harassing the calculator...")
            print(txt)
    match choice:
        case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8:
            c = COLORS[choice]
            return c[1]
        case _:
            return DEFAULT
