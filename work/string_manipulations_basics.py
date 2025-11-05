import locale
import pyperclip
locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')

def printPicnic(items: dict, left_width: int, right_width: int ) -> None:
    print("PICNIC ITEMS".center(left_width + right_width, "-"))
    for key, value in items.items():
        print(key.ljust(left_width, ".") + str(value).rjust(right_width))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)


def printMenu(items: dict, left_width: int, right_width: int) -> None:
    print("MENU".center(left_width + right_width, "-"))
    for key, value in items.items():
        print(key.ljust(left_width, ".") + str(value).rjust(right_width))

menu = {'Pizza Margherita': 7.50, 'Lasagne': 9.00, 'Tiramisu': 4.50, 'Espresso': 2.00}
printMenu(menu, 20, 6)

def printScores(data: dict)->None:
    LEFT_WIDTH, RIGHT_WIDTH = 12, 10
    print("PLAYER".ljust(LEFT_WIDTH ) + "SCORE".rjust(RIGHT_WIDTH))
    print("-".center(LEFT_WIDTH + RIGHT_WIDTH, "-"))
    for key, value in data.items():
        print(key.ljust(LEFT_WIDTH, " ") + str(value).rjust(RIGHT_WIDTH))

    

scores = {'Alice': 2500, 'Bob': 1870, 'Carla': 3250}
printScores(scores)


def printPriceList(prices: list[tuple[str, float]]) -> None:
    LEFT_WIDTH, RIGHT_WIDTH = 9, 10
    for tuple_pair in prices:
        item, price = tuple_pair
        price_local = locale.currency(price, grouping=True)
        print(item.ljust(LEFT_WIDTH, " ") + ":".center(1)
              + f"{price_local}".rjust(RIGHT_WIDTH))


items = [('Brot', 2.5), ('Butter', 1.25), ('Käse', 3.99), ('Milch', 1.1)]
printPriceList(items)

pyperclip.copy('Hello world!')
print(pyperclip.paste())