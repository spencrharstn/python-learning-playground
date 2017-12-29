def count_earnings():
    print("This is a simple script to help tipped workers count their earnings in US dollars.\n"
             "Please only input integers.\n")
    denominations = ['ones', 'fives', 'tens', 'twenties', 'fifties', 'hundreds']
    values = [1, 5, 10, 20, 50, 100]
    total = 0
    for val, denom in zip(values, denominations):
        while True:
            try:
                total += val * int(input("Type in how many {} there are: ".format(denom)))
            except ValueError as e:
                print("Input must be an integer")
                continue
            else:
                break
        
    return "{}${:,.2f}".format(["","-"][total<0], abs(total))

if __name__ == "__main__":
    print(count_earnings())