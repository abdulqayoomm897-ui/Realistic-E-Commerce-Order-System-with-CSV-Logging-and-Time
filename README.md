# 🛒 Order Management System

A simple Python-based order management system that:

Reads product details from a products.csv file.

Allows adding items to an order by product ID.

Applies discounts at the class level.

Logs every method call into a log.txt file using a decorator.

## 📖 Features

✅ Add products by ID (reads from products.csv)

✅ Automatic logging of method calls (log.txt)

✅ Apply discounts to all orders using a class method

✅ Calculate subtotal and final total after discount

✅ Gracefully handles invalid product IDs

## 📂 Project Structure
📦 order-management
 ┣ 📜 order.py          # Main Python file (your code)
 ┣ 📜 products.csv      # Product list (ID, Name, Price)
 ┣ 📜 log.txt           # Execution log (auto-generated)
 ┣ 📜 README.md         # Project documentation

📊 Example products.csv File

Make sure you have a products.csv file in the same folder with this format:

Example product.csv,
id,name,price
1,Laptop,1200
2,Phone,800
3,Headphones,150
4,Mouse,40
5,Keyboard,60


# ⚡ Usage
1️⃣ Clone the repository
git clone https://github.com/your-abdulqayoomm897-ui/order-management.git
cd order-management

2️⃣ Run the program
python order.py

3️⃣ Sample Output
Added 2 × Laptop (ID 1)
Added 3 × Phone (ID 4)
Product ID 99 not found!
Final total: 5.85

## 📝 Logging

Every decorated function is logged in log.txt with timestamps:

2025-08-24 20:10:05.345 Running..'add_item_by_id'...
2025-08-24 20:10:05.347 Finished..'add_item_by_id'...

🔧 Methods Explanation
Method	Type	Description
add_item_by_id(id, qty)	Instance method	Adds an item to order by looking it up in products.csv.
calculate_total()	Instance method	Calculates subtotal and applies discount if set.
set_discount(rate)	Class method	Sets discount percentage for all orders.
logger	Decorator	Logs function start and end into log.txt.

## Abdul Qayoom Mangi
