"""Pizza ordering system"""

# pizza
pizzas = {} #dictionary of pizzas
order_num = 1 #order number
print("Enter 'q' anytime to quit")
while True:
    new_pizza = {} # new dictionary defining a pizza
    prompt = "What size of pizza? (large, medium or small) "
    size = input(prompt)
    if size == 'q':
        break
    prompt = "What crust? (thin, thick, gluten-free) "
    crust = input(prompt)
    if crust == 'q':
        break

    toppings = [] #list of toppings
    print("Please add toppings. 's' to stop adding toppings")
    while True:
        topping = input("\tTopping: ")
        if topping == 's' or topping == 'q':
            break
        toppings.append(topping)

    new_pizza = {
        'size': size,
        'crust': crust,
        'toppings': toppings
    }

    pizzas[order_num] = new_pizza
    order_num += 1

print("The pizzas to create is: ")
for order_num, pizza in pizzas.items():
    print("Order #: " + str(order_num))
    print(" Size: " + pizza['size'].title())
    print(" Crust: " + pizza['crust'].title())
    print(" Toppings: ")
    for topping in pizza['toppings']:
        print("\t" + topping.title())
    input("Press enter to continue...")