print('Sales Report:')
print()
while True:
    try:
        year = int(input('Input the year the sales report is for: '))
        break
    except ValueError:
        print('Invalid input, please input year.')
print()

sales_list = []

for month in range(1, 13):
    while True:
        try:
            sales = float(input(f'Enter the sales for the month {month}: £'))
            break
        except ValueError:
            print('Invalid input. Please enter valid sales amount.')
    sales_list.append(sales)

total_sales = sum(sales_list)
average_sales = total_sales // 12
max_sales = max(sales_list)
min_sales = min(sales_list)

print()
print(f'Total sales for {year}: £{total_sales}')
print(f'Average sales: £{average_sales}')
print(f'Maximum sales: £{max_sales}')
print(f'Minimum sales: £{min_sales}')
