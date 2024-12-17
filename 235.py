def print_square(h, w, symbol, user_filled):
    for i in range(h):
        if user_filled == "y":
            print(symbol * w)
        else:
            if i == 0 or i == h - 1:
                print(symbol * w)
            else:
                print(symbol + " " * (w - 2) + symbol)

h = int(input("Enter the height of the square: "))
w = int(input("Enter the width of the square: "))
symbol = input("Enter symbol for square: ")
user_filled = input("Is the square filled (y/n)? ")
print_square(h, w, symbol, user_filled)

