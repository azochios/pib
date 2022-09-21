from math import ceil
# Fluid volume units
# 8 fl.oz to quart ratio
FLOZ_TO_QT = 4
QT_TO_GAL  = 4

# Distance and Surface units
# Sq.ft coverage per 8fl.oz (the minimum container volume).
SQ_FT_COVERAGE = 350 / (FLOZ_TO_QT * QT_TO_GAL)

# NAME, CONTAINERS (units), FL.OZ, PRICE
PAINT = [
    "BEHR DYNASTY",
    ['5gal', '1gal', '1qt', '8oz'],
    [80, 16, 4, 1],
    [297.0, 62.98, 28.98, 6.48]
]

# Calculate the volume of the paint needed
def volCalc(area):
    floz = ceil(area / SQ_FT_COVERAGE)
    return floz

def costCalc(floz):
    # First, calculate how many containers of each quantity
    containers = []

    for x in PAINT[2]:
        quotient = floz // x
        containers.append(quotient)

        if quotient == 0:
            continue
        else:
            floz %= x
    # Then calculate cost
    cost = []
    
    for i in range(len(containers)):
        cost.append(containers[i] * PAINT[3][i])
    
    return [containers, cost]
        
