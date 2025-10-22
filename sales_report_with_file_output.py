print('Sales Report:')
print()
year = int(input('The year the sales report is for: '))
print()

sales_list = []

with open('sales.txt', 'wt') as file:

    file.write('Sales Report:\n')
    file.write('--------------\n\n')
    file.write(f'Sales report is for {year}\n\n')

    for month in range(1, 13):
        while True:
            try:
                sales = float(input(f'Enter the sales for the month {month}: £'))
                break
            except ValueError:
                print('Invalid input. Please enter valid sales amount.')

        file.write(f'Month {month}: £{sales}\n')

        sales_list.append(sales)

    total_sales = sum(sales_list)
    average_sales = total_sales / 12
    max_sales = max(sales_list)
    min_sales = min(sales_list)

    file.write('\n')
    file.write('Summary:\n')
    file.write('---------\n')
    file.write(f'\nTotal sales for {year}: £{total_sales}\n')
    file.write(f'Average sales: £{average_sales}\n')
    file.write(f'Maximum sales: £{max_sales}\n')
    file.write(f'Minimum sales: £{min_sales}\n')

print()
print(f'Total sales for {year}: £{total_sales}')
print(f'Average sales: £{average_sales}')
print(f'Maximum sales: £{max_sales}')
print(f'Minimum sales: £{min_sales}')
