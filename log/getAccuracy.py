from sys import argv
if len(argv) != 2 :
    print("pleas use correctly")
else:
    file = open(argv[1], "r")
    stats = file.readlines()
    denominator = 0
    numerator = 0
    for element in stats:
        if element == "2\n" :
            numerator = numerator +1;
        denominator = denominator +1;
    print(numerator/denominator, numerator, denominator)
