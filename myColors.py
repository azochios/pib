COLORS = {
    1 : ["000000", "paint it black"],
    2 : ["0000AA", "insidious blue"],
    3 : ["00AA00", "fiery green"],
    4 : ["00AAAA", "viscious cyan"],
    5 : ["AA0000", "redemption dead red"],
    6 : ["AA00AA", "deep purple"],
    7 : ["AA5500", "merry yellow"],
    8 : ["AAAAAA", "fluffy white"]
}

DEFAULT = "paint it black"

def printColors():
    for k, v in COLORS.items():
        print(f"{k}) {v[1]}")

def pickColor(question):
    print(f"Please choose a color (1-8) for {question}:")
    printColors()
    choice = int(input())

    match choice:
        case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8:
            c = COLORS[choice]
            return c[1]
        case _:
            return DEFAULT