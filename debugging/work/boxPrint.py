def exception_prove(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("symbol must be a single character")
    if width <= 2:
        raise Exception("width must be greater than 2")
    if height <= 2:
        raise Exception("height must be greater than 2")
    else:
        return True


def boxPrint(symbol, width, height):
    if exception_prove(symbol, width, height):
        print(symbol* width)
        for i in range (height-2):
            print(symbol +(" " * (width-2))+ symbol)
        print(symbol*width)

for syn, w, h in (("*", 4,4), ("O",20,5),("x",1,3),("ZZ", 3, 3,)):
    try:
        boxPrint(syn, w, h)
    except Exception as ex:
        print("An Exception happened: " + str(ex))