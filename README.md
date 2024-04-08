# CSARCH2 X22 - Simulation Project

## Contents
- [Introduction](https://github.com/michhandreaa/CSARCH2-Binary64FloatingPointConverterSimulationProject?tab=readme-ov-file#introduction)
- [Video Demonstration](https://github.com/michhandreaa/CSARCH2-Binary64FloatingPointConverterSimulationProject?tab=readme-ov-filed#video-demonstration)
- [Test Cases](https://github.com/michhandreaa/CSARCH2-Binary64FloatingPointConverterSimulationProject?tab=readme-ov-file#test-cases)
- [Source Code](https://github.com/michhandreaa/CSARCH2-Binary64FloatingPointConverterSimulationProject?tab=readme-ov-file#source-code)
- [Analysis Writeup](https://github.com/michhandreaa/CSARCH2-Binary64FloatingPointConverterSimulationProject?tab=readme-ov-file#analysis-writeup)
- [Key Takeaways](https://github.com/michhandreaa/CSARCH2-Binary64FloatingPointConverterSimulationProject?tab=readme-ov-file#key-takeaways)

## Introduction

### About the App:
This simulation project is a stand-alone IEEE-754 Binary-64 Floating Point Converter. The project was made using Python and using tkinter library for the GUI. 

### Members:
- Martinez, Michelle Andrea H.
- Rojo, Kate Lynn M.
- Romblon, Kathleen Mae V.
- Tipon, Joshua Emmanuel G.

### Task
#### Topic: 
IEEE-754 Binary-64 floating point converter (including all special cases)
- Input: (1) binary mantissa and base-2 (i.e., 101.01x25) (2) Decimal and base-10 (i.e. 65.0x103). Also should support special cases (i.e., NaN).
- Output: (1) binary output with space between section (2) its hexadecimal equivalent (3) with option to output in text file.

#### Application platform:
- Stand-alone with GUI (graphics user interface) using a library in python called tkinter

#### Programming language: 
- Python

#### How to Run the Program:

##### Step 1: 
Run .bat file for easier downloading of the libraries used and to run the app

##### Step 2:
Try the app -- do different test cases

##### Step 3:
Print the result

## Video Demonstration 
[Link to Video](https://github.com/michhandreaa/CSARCH2-Binary64FloatingPointConverterSimulationProject/)

* insert github link redirecting to short video location - (Showing program compilation is correct and showing all test cases that will cover the specifications (normal, special case, different inputs, etc.)

## Test cases:
[Link to screenshots](https://github.com/michhandreaa/CSARCH2-Binary64FloatingPointConverterSimulationProject/)

### Test Case 1: Positive binary mantissa and base-2
- Screenshot of the program output
![image](https://github.com/michhandreaa/CSARCH2-Binary64FloatingPointConverterSimulationProject/assets/106814132/9a4473ea-33fd-4f34-bf7f-c7c80ef212c5)
- Input: 1.00111x2<sup>5</sup>
- Outputs:
   - Sign: 0
   - Exponent Representation: 100 000 00001
   - Mantissa: 0011 1000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
   - Binary Representation: 0b0100 0000 0100 0011 1000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
   - Hexadecimal Representation: 0x4043800000000000

### Test Case 2: Negative binary mantissa and base-2
- Screenshot of the program output
  ![image](https://github.com/michhandreaa/CSARCH2-Binary64FloatingPointConverterSimulationProject/assets/106814132/b2cb8e42-3a8a-471e-b0d3-f061870d16e3)
- Input: -10000.0001x2<sup>4</sup>
- Outputs:
   - Sign: 1
   - Exponent Representation: 100 0000 0111
   - Mantissa: 0000 0001 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
   - Binary Representation: 0b1100 0000 0111 0000 0001 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
   - Hexadecimal Representation: 0xC070100000000000
  
### Test Case 3: Positive decimal and base-10 
- Screenshot of the program output
 ![image](https://github.com/michhandreaa/CSARCH2-Binary64FloatingPointConverterSimulationProject/assets/106814132/797395d5-ac33-49c3-bf4e-c05e876cae54)
- Input: 65.0x10<sup>3</sup>
- Outputs:
   - Sign: 0
   - Exponent Representation: 100 0000 1110
   - Mantissa: 1111 1011 1101 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
   - Binary Representation: 0b0100 0000 1110 1111 1011 1101 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
   - Hexadecimal Representation: 0x40EFBD0000000000

### Test Case 4: Negative decimal and base-10 
- Screenshot of the program output
  ![image](https://github.com/michhandreaa/CSARCH2-Binary64FloatingPointConverterSimulationProject/assets/106814132/4af3a853-6686-43bd-b241-d9854f7a31e4)
- Input: -88.75x10<sup>6</sup>
- Outputs:
   - Sign: 1
   - Exponent Representation: 100 0001 1000
   - Mantissa: 0101 0010 1000 1101 1110 1100 0000 0000 0000 0000 0000 0000 0000
   - Binary Representation: 0b1100 0001 1000 0101 0010 1000 1101 1110 1100 0000 0000 0000 0000 0000 0000 0000
   - Hexadecimal Representation: 0xC18528DEC0000000

### Test Case 5:  Binary Positive 0 
- Screenshot of the program output

- Input: 
- Outputs:
   - Sign: 
   - Exponent Representation: 
   - Mantissa:
   - Binary Representation: 
   - Hexadecimal Representation: 

### Test Case 6:  Binary Negative 0 
- Screenshot of the program output
- Input: 
- Outputs:
   - Sign: 
   - Exponent Representation: 
   - Mantissa:
   - Binary Representation: 
   - Hexadecimal Representation: 

### Test Case 7:  Decimal Positive 0 
- Screenshot of the program output
- Input: 
- Outputs:
   - Sign: 
   - Exponent Representation: 
   - Mantissa:
   - Binary Representation: 
   - Hexadecimal Representation: 

### Test Case 8:  Decimal Negative 0 
- Screenshot of the program output
- Input: 
- Outputs:
   - Sign: 
   - Exponent Representation: 
   - Mantissa:
   - Binary Representation: 
   - Hexadecimal Representation: 

### Test Case 9: Special case infinity
- Screenshot of the program output
- Input: 
- Outputs:
   - Sign: 
   - Exponent Representation: 
   - Mantissa:
   - Binary Representation: 
   - Hexadecimal Representation: 

### Test Case 10: Special case denormalized
- Screenshot of the program output
- Input: 
- Outputs:
   - Sign: 
   - Exponent Representation: 
   - Mantissa:
   - Binary Representation: 
   - Hexadecimal Representation: 

### Test Case 11: Special case SNaN
- Screenshot of the program output
- Input: 
- Outputs:
   - Sign: 
   - Exponent Representation: 
   - Mantissa:
   - Binary Representation: 
   - Hexadecimal Representation: 

### Test Case 12: Special case QNaN
- Screenshot of the program output
- Input: 
- Outputs:
   - Sign: 
   - Exponent Representation: 
   - Mantissa:
   - Binary Representation: 
   - Hexadecimal Representation: 
  
### Test Case 13: None of the above (error catching)
- Screenshot of the program output
- Input: 
- Outputs:
   - Sign: 
   - Exponent Representation: 
   - Mantissa:
   - Binary Representation: 
   - Hexadecimal Representation: 

## Source Code
[Link to source code](https://github.com/michhandreaa/CSARCH2-Binary64FloatingPointConverterSimulationProject/)

## Analysis Writeup
[Link to analysis writeup](https://github.com/michhandreaa/CSARCH2-Binary64FloatingPointConverterSimulationProject/)

## Key Takeaways
