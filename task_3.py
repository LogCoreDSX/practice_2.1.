import csv


def say(say_param):
    if say_param == "void":
        print(" ")
    elif say_param == "start":
        print(" ")
        print("<---- Start program ---->")
    elif say_param == "end":
        print(" ")
        print("<---- End program ---->")
    elif say_param == "er_num":
        print("<Error. ONLY Number !>")
    elif say_param == "notmod":
        print("<Not FOUND mode>")
    elif say_param == "notfile":
        print("<File NOT FOUND>")
    elif say_param == "cancel":
        print(" ")
        print("<Canceling>")
    elif say_param == "empty":
        print("<No products in list>")


def read_csv(filename):
    products = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    product = {
                        'name': row[0],
                        'price': float(row[1]),
                        'quantity': int(row[2])
                    }
                    products.append(product)
        print(f"<Loaded {len(products)} products>")
    except FileNotFoundError:
        say("notfile")
        print("<Creating new file>")
        with open(filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Название', 'Цена', 'Количество'])
    except Exception as e:
        print(f"<Error: {e}>")
    return products


def save_csv(filename, products):
    try:
        with open(filename, 'w', encoding = 'utf-8', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(['Название', 'Цена', 'Количество'])
            for product in products:
                writer.writerow([product['name'], product['price'], product['quantity']])
        print(f"<Saved {len(products)} products to file>")
    except Exception as e:
        print(f"<Error saving: {e}>")


def add_product(products):
    say("void")
    print("-- Add New Product --")
    say("void")
    name = input("Product name: ").strip()
    if not name:
        print("<Name cannot be empty>")
        return products
    while True:
        try:
            price = float(input("Price: "))
            if price < 0:
                print("<Price cannot be negative>")
                continue
            break
        except ValueError:
            say("er_num")
    while True:
        try:
            quantity = int(input("Quantity: "))
            if quantity < 0:
                print("<Quantity cannot be negative>")
                continue
            break
        except ValueError:
            say("er_num")
    new_product = {
        'name': name,
        'price': price,
        'quantity': quantity
    }
    products.append(new_product)
    say("void")
    print(f"<Product '{name}' added>")
    return products


def search_product(products):
    if not products:
        say("empty")
        return
    say("void")
    search_term = input("Enter product name to search: ").strip().lower()
    found = []
    for product in products:
        if search_term in product['name'].lower():
            found.append(product)
    say("void")
    if found:
        print(f"Found {len(found)} product(s):")
        say("void")
        print(f"{'№':<3} {'Название':<15} {'Цена':<10} {'Количество':<10} {'Стоимость':<10}")
        print("-" * 60)
        for i, p in enumerate(found, 1):
            total = p['price'] * p['quantity']
            print(f"{i:<3} {p['name']:<15} {p['price']:<10.2f} {p['quantity']:<10} {total:<10.2f}")
    else:
        print("<No products found>")


def calculate_total(products):
    if not products:
        say("empty")
        return 0
    
    total_sum = 0
    say("void")
    print("-- Stock Value Calculation --")
    say("void")
    print(f"{'Название':<15} {'Цена':<10} {'Количество':<10} {'Стоимость':<10}")
    print("-" * 50)
    for product in products:
        total = product['price'] * product['quantity']
        total_sum += total
        print(f"{product['name']:<15} {product['price']:<10.2f} {product['quantity']:<10} {total:<10.2f}")
    print("-" * 50)
    print(f"{'ИТОГО:':<37} {total_sum:<10.2f}")
    say("void")
    return total_sum


def view_products(products):
    if not products:
        say("empty")
        return
    say("void")
    print("-- Product List --")
    say("void")
    print(f"{'№':<3} {'Название':<15} {'Цена':<10} {'Количество':<10}")
    print("-" * 45)
    for i, p in enumerate(products, 1):
        print(f"{i:<3} {p['name']:<15} {p['price']:<10.2f} {p['quantity']:<10}")
    print("-" * 45)
    print(f"Total products: {len(products)}")


#Главная часть
say("start")
say("say")
filename_main = "result/products.csv"
products_main = read_csv(filename_main)
while True:
    say("void")
    print("--- CSV PRODUCT MANAGER ---")
    say("void")
    print("<0> View all products")
    print("<1> Add new product")
    print("<2> Search product")
    print("<3> Calculate total value")
    print("<4> Save to file")
    print("<5> Exit")
    say("void")
    try:
        mode = int(input("Select mode: "))
    except ValueError:
        say("er_num")
        continue
    match mode:
        case 0: view_products(products_main)
        case 1: products_main = add_product(products_main)
        case 2: search_product(products_main)
        case 3: calculate_total(products_main)
        case 4: save_csv(filename_main, products_main)
        case 5:
            say("void")
            save = input("Save before exit? (y/n) : ").lower()
            if save == 'y':
                save_csv(filename_main, products_main)
            say("end")
            break
        case _:
            say("notmod")