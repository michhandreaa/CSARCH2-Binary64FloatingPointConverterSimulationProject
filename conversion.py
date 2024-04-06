class ConversionSimulatorLogic:
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

        # TODO: Separate whole number from fraction
        whole, fraction = str(input_text).split(".")
        whole = int(whole)
        fraction = int(fraction) / 10 ** len(fraction)

        # TODO: Convert whole number to binary
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
        print(binary_number)

        # TODO: Prepend the sign bit to the binary number
        signed_binary = sign_bit + binary_number
        print(signed_binary)


    def convert_to_hexadecimal(input_text, step_by_step=False):
        pass  # Implement hexadecimal conversion logic

    def save_to_file(binary_result, hex_result):
        pass  # Implement save to file logic
