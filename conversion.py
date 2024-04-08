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

        if input_text.count('.') == 1: # if inputted text has BOTH whole and fraction    
            # TODO: Separate whole number from fraction
            whole, fraction = str(input_text).split(".")
            fraction_size_limit = 52-(len(whole)-1)
            cnt = 0
            whole = int(whole)
            fraction = int(fraction) / 10 ** len(fraction)

            # TODO: Convert fraction number to binary
            converted_binary = bin(whole).lstrip("0b") + "."

            while fraction != 0 and cnt <= fraction_size_limit:

                # print(binary_number, fraction)
                fraction = fraction * 2
                if fraction >= 1:
                    fraction = fraction - 1
                    converted_binary = converted_binary + "1"
                else:
                    converted_binary = converted_binary + "0"
            
            cnt += 1

        elif input_text.count('.') == 0: # if inputted text only has whole
            whole = int(input_text)
            converted_binary = "0"

        # # TODO: Prepend the sign bit to the binary number
        # converted_binary = sign_bit + binary_number

        # Remove "0b" prefix if present
        converted_binary = converted_binary.replace("0b", "")
# 
        return converted_binary
    
    # Convert decimal input from scientific notation to whole number (# x 10^0)
    def descientific_decimal(decimal_whole, decimal_exponent):
        descientify = float(decimal_whole) * (10**int(decimal_exponent))
        
        return descientify

# DONE
    # Calculate the base-2 exponent using the change of base formula
    def convert_base10_to_base2_exponent(base10_exponent):
        
        base2_exponent = int(base10_exponent) * math.log2(10)
        converted_exponent = math.floor(base2_exponent)

        return converted_exponent
    
# DONE
    def normalize(mantissa,  exponent):
        # ------------ NORMALIZE ------------

        exponent = int(exponent)
        new_mantissa = mantissa.replace('.', '')
        
        #Find the index of the first '1' in the mantissa
        one_index = new_mantissa.find('1')
        
        #Move the decimal point to just after this '1'
        new_mantissa = new_mantissa[:one_index+1] + '.' + new_mantissa[one_index+1:]
        
        #Adjust the exponent based on the movement of the decimal point
        if mantissa[0] == '-':
            dot_index = mantissa.find('.') - 1
            
        else:
            dot_index = mantissa.find('.')
            
        exponent += dot_index - (one_index+1)
        
        #Remove any leading or trailing zeroes
        new_mantissa = new_mantissa.strip('0')
        
        return new_mantissa, exponent


    ### assuming binary input
    def converter64(mantissa, exponent):

        mantissa = str(mantissa)
        exponent = int(exponent)

        # ------------ SIGN BIT ------------
        # mantissa and exponent are str
        if mantissa[0] == '-':
            sign = 1
            mantissa = mantissa[1:] # removes (-) sign

        else:
            if mantissa[0] == '+':
                mantissa = mantissa[1:] # removes (+) sign
            sign = 0

        # ------------ NORMALIZE ------------

        new_mantissa, exponent = ConversionSimulatorLogic.normalize(mantissa, exponent)
        
        # ------------ e' ------------ 
        # e' (11 bits)
        e_prime = exponent + 1023
        # convert e_prime to binary
        e_prime = bin(e_prime)[2:].zfill(11)
        
        # ------------ f ------------
        # f (52 bits)
        f = new_mantissa.replace('.', '')  # Remove '.' from mantissa
        f = new_mantissa[2:] # excludes 1.
        f = f.ljust(52, '0')  # Right-pad with zeros to make it 52 bits

                        
        return str(sign), str(e_prime), str(f)

    def convert_to_hexadecimal(input_text):

        # Initialize an empty string to store the hexadecimal result
        hex_result = ''

        for i in range(len(input_text) // 4):
            # Extract a group of four binary digits
            group = input_text[-4:]
            
            # Convert the group to its corresponding hexadecimal digit
            hex_digit = hex(int(group, 2))[2:].upper()
            
            # Prepend the hexadecimal digit to the result
            hex_result = hex_digit + hex_result
            
            # Move to the next group of four binary digits
            input_text = input_text[:-4]

        return hex_result