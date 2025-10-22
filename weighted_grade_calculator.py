from input_functions import get_float

total_weighted_mark = 0

def get_float_input(message):
    return get_float(f"{message} (in percentage): ")

def get_input_and_check_weight(message):
    mark = get_float_input(message)
    weight = get_float_input('Input the weight of the mark')

    if not 0 <= weight <= 100:
        print('Invalid weight. Please enter a percentage between 0 and 100.')
        return None, None

    return mark, weight

print('Mark calculator\n')

mark_one, weight_one = get_input_and_check_weight('Input the first mark')
mark_two, weight_two = get_input_and_check_weight('\nInput the second mark')
mark_three, weight_three = get_input_and_check_weight('\nInput the third mark')

if None in (mark_one, mark_two, mark_three):
    exit()

weighted_mark_one = (mark_one * weight_one) / 100
weighted_mark_two = (mark_two * weight_two) / 100
weighted_mark_three = (mark_three * weight_three) / 100
total_weighted_mark += weighted_mark_one + weighted_mark_two + weighted_mark_three
overall_grade = round(total_weighted_mark, 2)

print('\nThe overall mark for the marks and weight input is:')
print(f'Mark 1 = {mark_one} Weight 1 = {weight_one}% Weighted mark = {mark_one} x {weight_one}% = {weighted_mark_one}%')
print(f'Mark 2 = {mark_two} Weight 2 = {weight_two}% Weighted mark = {mark_two} x {weight_two}% = {weighted_mark_two}%')
print(f'Mark 3 = {mark_three} Weight 3 = {weight_three}% Weighted mark = {mark_three} x {weight_three}% = {weighted_mark_three}%\n')
print(f'Overall mark is: {weighted_mark_one}% + {weighted_mark_two}% + {weighted_mark_three}% = {overall_grade}%')
