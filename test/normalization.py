def normalization_test(mantissa, exponent):

    # exponent = int(exponent)

    # # Step 1: Look for '.'
    # dot_index = mantissa.find('.')

    # # if no '.', add one to the right-most part of the string
    # if '.' not in mantissa:
    #     mantissa += '.'

    # # Step 2: Check if '1.' is in the leftmost part of the string
    # if not mantissa.startswith('1.'):
    #     new_mantissa = ""
    #     found_target = False
        
    #     whole, fraction = str(mantissa).split(".")

    #     mantissa = whole + fraction

    #     ''' Step 3a: check if there is a '1" anywhere on left side portion of current whole part.
    #                     if there is, iterate through each char until encounter FIRST "1" then insert a "."
    #     '''   
    #     for index, one in enumerate(whole):
    #         #check left:
    #         new_mantissa += one 
    #         if one == "1" and not found_target:
    #             new_mantissa += "."
    #             found_target = True
    #             # new_mantissa = new_mantissa+fraction
    #             new_mantissa += fraction

    #     # Step 4a: If new "." was inserted to whole, add 
    #     # exponent = (dot_index-index) + exponent# if left add
    #     if found_target:
    #         exponent += (dot_index - index) # if left add
        
    #     ''' Step 3b: check if there is a '1" anywhere on right side portion of current fraction part.
    #                     if there is, iterate through each char until encounter FIRST "1" then insert a "."
    #     '''     
    #     if not found_target:
    #         for index, one in enumerate(fraction):
    #             new_mantissa += one
    #             if one == "1" and not found_target:
    #                 new_mantissa += "."
    #                 # Step 4a: If new "." was inserted in fraction, subtract 
    #                 # exponent = (dot_index-index) - exponent# if right subtact
    #                 exponent -= (dot_index - index) # if right subtract
    #                 found_target = True
    #     #Normalize the mantissa
    #     if new_mantissa[1] == '0':
    #         new_mantissa = new_mantissa[2:]
    #         exponent += 1
        
    #     return new_mantissa, exponent
    
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
        
    exponent += dot_index - one_index
    
    #Remove any leading or trailing zeroes
    new_mantissa = new_mantissa.strip('0')
    
    return new_mantissa, exponent

mantissa = input("Enter mantissa (in binary): ")
exponent = input("Enter exponent (in binary): ")

new_mantissa, new_exponent = normalization_test(mantissa, exponent)
print("Normalized number: ", new_mantissa)
print("exponent number: ", new_exponent)