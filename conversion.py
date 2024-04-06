class ConversionSimulatorLogic:
    def convert_to_binary(input_text):
        return bin(int(input_text))
        
        # Implement binary conversion logic

    def convert_to_hexadecimal(input_text, step_by_step=False):
        pass  # Implement hexadecimal conversion logic
    
    def converter64(mantissa, exponent):
        ### assuming binary input
        # mantissa and exponent are str
        if mantissa[0] == '-':
            sign = 1
            mantissa.pop(0) # removes (-) sign
        else:
            sign = 0
            
        index = 0
        # normalize, find "."
        while index < len(mantissa):
            if mantissa[0] == "1":
                mantissa.insert(1, ".")
                break
            else:
                mantissa.pop(0)
                index += 1
        
        # e' (11 bits)
        e_prime = exponent + 1023
        # convert e_prime to binary
        e_prime = bin(e_prime)[2:].zfill(11)
        
        # f (52 bits)
        f = []
        f = mantissa[2:] # excludes 1.
        while len(f) < 53:
            f.append(0)
        
        return sign, e_prime, f

    def save_to_file(binary_result, hex_result):
        pass  # Implement save to file logic
