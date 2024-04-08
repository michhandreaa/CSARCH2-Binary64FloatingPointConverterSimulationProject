import tkinter as tk
import math

# LOGIC FUNCTIONS -- LOGIC SKELETON IS DEF RUN_SIMULATION IN MAIN.PY
class ConversionSimulatorLogic:

    # DONE
    def is_float(input_string, exponent_string):  # checking if input is numeric after removing . and exponent is numeric
        if input_string.replace(".", "").isnumeric() and exponent_string.isnumeric():
            return True
        else:
            return False

    # DONE
    def validateInput(input_text, exponent, type, result_text):  # checking if input is positive or negative and if is_float

        if str(input_text)[0] == "+" or str(input_text)[0] == "-":
                # Remove the '+' or '-' character
                input_text = input_text[1:]

        if type == "Binary" and not all(char in '01.' for char in input_text) and input_text.count('.') <= 1:
            result_text.insert(tk.END, "\nInvalid input! Please try again. \n Hint: Only 0s and 1s for mantissa.\n")
            return False

        if ConversionSimulatorLogic.is_float(input_text, exponent) == False:
            result_text.insert(tk.END, "\nInvalid input! Please try again.\n Hint 1: Only numbers are allowed.\n Hint 2: Exponent should be a whole number \n")

            return False
        
        return True
    
    # assume correct decimal and exponent inputs
    def convert_to_binary(input_text):

        # TODO: Get Sign Bit and remove from input string
        if str(input_text)[0] == '+' or str(input_text)[0] == '-':
            if str(input_text)[0] == '-':
                sign_bit = "1"
            else:
                sign_bit = "0"
            input_text = input_text[1:]
        else:
            sign_bit = "0"

        if input_text.count('.') == 1: # if inputted text has BOTH whole and fraction
        # TODO: Separate whole number from fraction
            whole, fraction = str(input_text).split(".")
            whole = int(whole)
            fraction = int(fraction) / 10 ** len(fraction)

            # TODO: Convert fraction number to binary
            binary_number = bin(whole).lstrip("0b") + "."

            while fraction != 0:
                # print(binary_number, fraction)
                fraction = fraction * 2
                if fraction >= 1:
                    fraction = fraction - 1
                    binary_number = binary_number + "1"
                else:
                    binary_number = binary_number + "0"

        elif input_text.count('.') == 0: # if inputted text only has whole
            whole = int(input_text)
            binary_number = "0"

        # TODO: Prepend the sign bit to the binary number
        converted_binary = sign_bit + binary_number

        return converted_binary

    # Calculate the base-2 exponent using the change of base formula
    def convert_base10_to_base2_exponent(base10_exponent):
        
        base2_exponent = int(base10_exponent) * math.log10(10) / math.log10(2)
        converted_exponent = round(base2_exponent)

        return converted_exponent
    
    

    def convert_to_hexadecimal(input_text, step_by_step=False):
        pass  # Implement hexadecimal conversion logic


    def save_to_file(binary_result, hex_result):
        pass  # Implement save to file logic