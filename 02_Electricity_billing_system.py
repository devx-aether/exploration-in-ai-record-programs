# Calculates slab-wise electricity charges for a given number of units
def calculate_bill(units):
    bill = 0
    if units <= 100:
        # First 100 units billed at Rs. 1.50 per unit
        bill = units * 1.50
    elif units <= 200:
        # First 100 units at 1.50 + remaining units (101 to 200) at 2.50
        bill = 100 * 1.50 + (units - 100) * 2.50
    elif units <= 500:
        # First 200 units covered above + units (201 to 500) at 4.00
        bill = (100 * 1.50) + (100 * 2.50) + (units - 200) * 4.00
    else:
        # First 500 units covered above + units above 500 at 6.00
        bill = (100 * 1.50) + (100 * 2.50) + (300 * 4.00) + (units - 500) * 6.00
    return bill


n = int(input("Enter number of customers: "))

# Loop once per customer from 1 to n
for i in range(1, n + 1):
    print(f"\nCustomer {i}")
    name = input("Enter customer name: ")
    # Use float so fractional unit readings are handled accurately
    units = float(input("Enter units consumed: "))
    bill = calculate_bill(units)
    print("Customer Name:", name)
    print("Units        :", units)
    # Round only for display; keep `bill` unrounded if reused later
    print("Bill Amount: Rs.", round(bill, 2))