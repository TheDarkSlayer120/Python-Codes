def get_float(prompt="Please enter a float: "):
    while True:
        user_input = input(prompt)
        try:
            float_value = float(user_input)
            return float_value
        except ValueError:
            print("Bad input. Please enter a valid float.")
