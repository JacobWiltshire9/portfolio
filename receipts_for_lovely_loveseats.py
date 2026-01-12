#Receipts for Lovely Loveseat Seats for Neat Suites on Fleet Street

#Lovely Loveseat Section

storeName = "Lovely Loveseat"
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = float(254.00)

#Stylish Settee Section

stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = float(180.50)

#Luxurious Lamp Section

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = float(52.15)

#Sales Area

sales_tax = float(.088) #8.8%

#First Customer

#Setting the variables with base values so you can add to them later on
customer_one_total = float(0)
customer_one_itemization = ""

#Calculates the total of items the customer wants to purchase
customer_one_total += lovely_loveseat_price + luxurious_lamp_price

#calculates customers total with tax
customer_one_tax = customer_one_total * sales_tax
customer_one_total += round(customer_one_tax, 2)

#Keeping track of customer's item description
customer_one_itemization += lovely_loveseat_description + " " + luxurious_lamp_description

#Printing the Receipt
print("Customer One Items: " + str(customer_one_itemization) + " " + """
Customer One Total : $""" + str(customer_one_total)) 

# AI Review - Your code implements the basic receipt workflow for Lovely Loveseats and prints a simple itemized total, aligning with the project goals.
# It defines item descriptions and prices, computes a running total with tax, and prints a receipt heading and total.
# Variable names are mostly descriptive, and the flow is easy to follow overall.
# The code directly sums fixed prices; for a small script this is fine and straightforward.
# Fix variable naming consistency to avoid NameError and ensure correct output. Consider computing tax separately and then adding to total, rather than mixing rounding at the end.