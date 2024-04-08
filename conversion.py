import tkinter as tk

class ConversionSimulatorLogic:

    def is_float(input_string, exponent_string):  # checking if input is remaining characters are numeric after removing .
        if input_string.replace(".", "").isnumeric() and exponent_string.isnumeric():
            return True
        else:
            return False

    def validateInput(input_text, exponent, type, result_text):  # checking if input is positive or negative and if is_float

        if str(input_text)[0] == "+" or str(input_text)[0] == "-":
                # Remove the '+' or '-' character
                input_text = input_text[1:]

        if type == "Binary" and not all(char in '01' for char in input_text):
            result_text.insert(tk.END, "\nInvalid input! Only 0s and 1s for mantissa.\n")
            return False

        if ConversionSimulatorLogic.is_float(input_text, exponent) == False:
            result_text.insert(tk.END, "\nInvalid input! Only numbers are allowed.\n")

            return False
        
        return True


    # Assume integer Decimal input
    def convert_to_binary(input_text):
        return bin(int(input_text))


    def convert_to_hexadecimal(input_text, step_by_step=False):
        pass  # Implement hexadecimal conversion logic


    def save_to_file(binary_result, hex_result):
        pass  # Implement save to file logic
