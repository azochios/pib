# Paint it Black, a paint calculator!

import myShape

SQ_FT_COVERAGE = 350
CM_TO_FT       = 30.48
CM_TO_M        = 100



width  = int(input("Enter width: "))
height = int(input("Enter height: "))

wall1 = myShape.Rectangle(width, height)

area = wall1.area / (CM_TO_FT ** 2)

paint = area / SQ_FT_COVERAGE
print(f'You will need {paint:.2f} gallons of paint!')

