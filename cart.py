def cartApplication(cart):
    if not cart:
        print("The cart is already empty!")
        return
    print("Shopping cart:")
    total = 0
    for i, item in enumerate(cart, start=1):
        print(f"{i}.{item['name']} : ${item['price']:.2f}")
        total += item['price']
    print(f"Total : ${total:.2f}")
def main():
    cart = []
    while True:
        print("\nShopping Application:")
        print("1. Add to cart item")
        print("2. View cart")
        print("3. Remove item from cart")
        print("4. Exit")
        choose = input("Enter your choice to perform: ")
        if choose == '1':
            item_name = input("Enter your item name: ")
            try:
                item_price = float(input("Enter the price: "))
            except ValueError:
                print("Invalid price! Please enter a number.")
                continue
            cart.append({'name': item_name, 'price': item_price})
            print("Item added to the cart.")
        elif choose == '2':
           cartApplication(cart)
        elif choose == '3':
            if not cart:
                print("The cart is already empty.")
            else:
                cartApplication(cart)
                try:
                    item_index = int(input("Enter the item number to remove: ")) - 1
                    if 0 <= item_index < len(cart):
                        removed = cart.pop(item_index)
                        print(f"Removed item: {removed['name']}")
                    else:
                        print("Invalid item number.")
                except ValueError:
                    print("Please enter a valid number.")
        elif choose == '4':
            print("Exit from the cart application.")
            break
        else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    main()