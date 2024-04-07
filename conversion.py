class ConversionSimulatorLogic:
    def convert_to_binary(input_text):
        return bin(int(input_text))
        
        # Implement binary conversion logic

    def convert_to_hexadecimal(input_text, step_by_step=False):
        return hex(int(input_text))
    
    
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
            
        binary_output = str(sign) + e_prime + f
        
        hex_output= hex(int(binary_output, 2))
        
        return {
            "sign": sign,
            "e_prime": e_prime,
            "f": f,
            "binary": binary_output,
            "hexadecimal": hex_output
        }

    def save_to_file(binary_result, hex_result):
        pass  # Implement save to file logic
