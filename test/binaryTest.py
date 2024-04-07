class ConversionSimulatorLogic:
    
    @staticmethod
    def convert_to_binary(input_text):
        return bin(int(input_text))[2:] 
    
        # Implement binary conversion logic

    def convert_to_hexadecimal(input_text, step_by_step=False):
        pass  # Implement hexadecimal conversion logic
        return hex(int(input_text, 2)) 
    
    @staticmethod
    def converter64(mantissa, exponent):
        ### assuming binary input
        # mantissa and exponent are str
        if mantissa[0] == '-':
            sign = 1
            # mantissa.pop(0) # removes (-) sign
            mantissa = mantissa[1:]
        else:
            sign = '0'
            
        # index = 0
        # normalize, find "."
        # while index < len(mantissa):
        #     if mantissa[0] == "1":
        #         mantissa.insert(1, ".")
        #         break
        #     else:
        #         mantissa.pop(0)
        #         index += 1
        
        # Normalize mantissa and find the decimal point
        mantissa = mantissa.strip('0')
        dot_index = mantissa.index('.') if '.' in mantissa else len(mantissa)
        
        mantissa += '0' * (52 - len(mantissa))
        # e' (11 bits)
        e_prime = int(exponent) + 1023
        e_prime_binary = format(e_prime, '011b')
        
        # e_prime = exponent + 1023
        # convert e_prime to binary
        # e_prime = bin(e_prime)[2:].zfill(11)
        
        # f (52 bits)
        # fraction_part = mantissa.replace('.', '')[:52]
        fraction_part = mantissa.split('.')[1][:52]  # Takes only the fraction part
        
        # f = []
        # f = mantissa[2:] # excludes 1.
        # while len(f) < 53:
        #     f.append(0)
        
        # return sign, e_prime, f
        
        # Combine all parts
        binary_representation = sign + ' ' + e_prime_binary + ' ' + fraction_part
        
        #Convert binary to hexadecimal
        hexadecimal_representation = hex(int(binary_representation.replace(' ', ''), 2))
        
        return binary_representation, hexadecimal_representation

    # def save_to_file(binary_result, hex_result):
        pass  # Implement save to file logic

# Input: 1.00111x25
    # Mantissa: 1.00111
    # Exponent: 5
# Output:
    # Binary:
    # Sign: 0
    # Exponent Representation: 100 0000 0100
    # Mantissa: 0011 1000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
    # Binary Representation: 0b0100 0000 0100 0011 1000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
    # Hexadecimal: 0x4043800000000000

    
# Test the implementation
mantissa = input("Enter mantissa (in binary): ") # 1.00111
exponent = input("Enter exponent (in base-2): ") # 5

binary,hexadecimal = ConversionSimulatorLogic.converter64(mantissa, exponent)
print("Sign:", binary[0]) # 0
print("Exponent Representation:", binary[2:13]) # 100 0000 0100
print("Mantissa:", binary[14:]) # 0011 1000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
print("Binary Representation:", binary.replace(' ', ' ')) # 0b0100 0000 0100 0011 1000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
print("Hexadecimal:", hexadecimal) #0x4043800000000000
