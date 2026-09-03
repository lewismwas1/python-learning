menu = [
    {
        "name": "Rice beef",
        "category": "main",
        "price": 50.99,
        "availability": True
    },
    {
        "name": "Chicken burger",
        "category": "main",
        "price": 45.99,
        "availability": True
    },
    {
        "name": "French fries",
        "category": "side",
        "price": 20.99,
        "availability": True
    },
    {
        "name": "Beef burger",
        "category": "main",
        "price": 60.99,
        "availability": False
    },
    {
        "name":"Chicken nuggets",
        "category": "side",
        "price": 20.99,
        "availability": False
    },
    {
        "name": "Coke",
        "category": "drink",
        "price": 10.99,
        "availability": True
    }
]
for food in menu:
    print(f"\nName: {food['name']}")
    print(f"Category: {food['category']}")
    print(f"Price: {food['price']}$")
    if not food['availability']:
        print("Sorry, this food is not available at the moment, PLEASE CHECK OUT OUR MENU FOR OTHER OPTIONS!")
    else:
        print("This food is available, MAKE YOUR ORDER NOW!")
