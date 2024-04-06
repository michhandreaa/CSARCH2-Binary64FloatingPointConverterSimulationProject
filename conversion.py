class ConversionSimulatorLogic:

    def is_float(string):
        if string.replace(".", "").isnumeric():
            return True
        else:
            return False


    def validateInput(input_text, type):
        try:
            if str(input_text)[0] == "+" or str(input_text)[0] == "-":
                # Remove the '+' or '-' character
                input_text = input_text[1:]

            if is_float(input_text) == False:
                raise InvalidInput
            return True
        except InvalidInput:
            print("Exception occured: Invalid input! Please only enter numerical digits as input.")
        return False


    # Assume integer Decimal input
    def convert_to_binary(input_text):
        return bin(int(input_text))


    def convert_to_hexadecimal(input_text, step_by_step=False):
        pass  # Implement hexadecimal conversion logic


    def save_to_file(binary_result, hex_result):
        pass  # Implement save to file logic
