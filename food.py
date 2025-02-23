import tkinter as tk
from tkinter import messagebox

# Food menu with prices
menu = {
    "Pizza": 8.99,
    "Burger": 5.99,
    "Pasta": 7.49,
    "Fries": 3.99,
    "Salad": 4.99,
    "Soda": 1.99
}

# Cart to store selected items
cart = {}

# Function to add items to the cart
def add_to_cart(item):
    if item in cart:
        cart[item] += 1
    else:
        cart[item] = 1
    update_cart()

# Function to remove items from the cart
def remove_from_cart(item):
    if item in cart:
        if cart[item] > 1:
            cart[item] -= 1
        else:
            del cart[item]
    update_cart()

# Function to update cart display
def update_cart():
    cart_display.delete(0, tk.END)
    total_price = 0
    for item, quantity in cart.items():
        price = menu[item] * quantity
        total_price += price
        cart_display.insert(tk.END, f"{item} x{quantity} - ${price:.2f}")
    total_label.config(text=f"Total: ${total_price:.2f}")

# Function to place an order
def place_order():
    if not cart:
        messagebox.showerror("Error", "Cart is empty! Add some items.")
        return

    order_summary = "Order Summary:\n"
    for item, quantity in cart.items():
        order_summary += f"{item} x{quantity} - ${menu[item] * quantity:.2f}\n"
    
    order_summary += f"\nTotal: ${sum(menu[item] * quantity for item, quantity in cart.items()):.2f}"
    
    messagebox.showinfo("Order Placed", order_summary)
    cart.clear()
    update_cart()

# Create main application window
app = tk.Tk()
app.title("Food Delivery System")
app.geometry("400x500")

# Menu label
tk.Label(app, text="Menu", font=("Arial", 14, "bold")).pack()

# Menu buttons
for food, price in menu.items():
    tk.Button(app, text=f"{food} - ${price:.2f}", command=lambda f=food: add_to_cart(f)).pack(pady=2)

# Cart Label
tk.Label(app, text="Your Cart", font=("Arial", 14, "bold")).pack()

# Cart display
cart_display = tk.Listbox(app, height=8)
cart_display.pack()

# Remove item button
tk.Button(app, text="Remove Selected", command=lambda: remove_from_cart(cart_display.get(tk.ACTIVE).split(" x")[0])).pack(pady=5)

# Total price label
total_label = tk.Label(app, text="Total: $0.00", font=("Arial", 12, "bold"))
total_label.pack()

# Place order button
tk.Button(app, text="Place Order", bg="green", fg="white", font=("Arial", 12, "bold"), command=place_order).pack(pady=10)

# Run application
app.mainloop()
