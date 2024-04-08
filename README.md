# CSARCH2 X22 - Simulation Project

## Contents
- [Introduction](https://github.com/michhandreaa/CSARCH2-Binary64FloatingPointConverterSimulationProject?tab=readme-ov-file#introduction)
- [Video Demonstration](https://drive.google.com/drive/folders/1vo1XsZO4flkhuDTrSAO25WQ6_eJbAzoJ?fbclid=IwAR18v4aD8gFXr5OAi47b4o2QzWRjyLqmDtnf1VTd-vw5kqFI5eyj6Qib1dM)
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
[Link to Video](https://drive.google.com/file/d/1hfoP7QvlU_zyE_VCve2NixsC7xWBLO09/view?usp=sharing)

## Test cases:

### Test Case 1: Positive binary mantissa and base-2
![image](https://github.com/michhandreaa/CSARCH2-Binary64FloatingPointConverterSimulationProject/assets/106814132/9a4473ea-33fd-4f34-bf7f-c7c80ef212c5)

### Test Case 2: Negative binary mantissa and base-2
![image](https://github.com/michhandreaa/CSARCH2-Binary64FloatingPointConverterSimulationProject/assets/106814132/b2cb8e42-3a8a-471e-b0d3-f061870d16e3)
  
### Test Case 3: Positive decimal and base-10 
![image](https://github.com/michhandreaa/CSARCH2-Binary64FloatingPointConverterSimulationProject/assets/106814132/797395d5-ac33-49c3-bf4e-c05e876cae54)

### Test Case 4: Negative decimal and base-10 
![image](https://github.com/michhandreaa/CSARCH2-Binary64FloatingPointConverterSimulationProject/assets/106814132/d0dac2f9-4b89-4559-9ffb-15fd4b03b198)

### Test Case 5:  Binary Positive 0 
![image](https://github.com/michhandreaa/CSARCH2-Binary64FloatingPointConverterSimulationProject/assets/106814132/9fc119df-35c2-4dba-b9df-9406aa8e5bab)

### Test Case 6:  Binary Negative 0 
![image](https://github.com/michhandreaa/CSARCH2-Binary64FloatingPointConverterSimulationProject/assets/106814132/38d58bed-d88a-4892-b319-4f3f7f114c35)

### Test Case 7:  Decimal Positive 0 
![image](https://github.com/michhandreaa/CSARCH2-Binary64FloatingPointConverterSimulationProject/assets/106814132/053e1060-71a1-4be2-b4f6-0405827dee2b)

### Test Case 8:  Decimal Negative 0 
![image](https://github.com/michhandreaa/CSARCH2-Binary64FloatingPointConverterSimulationProject/assets/106814132/8e112ac0-66f0-4dc6-893c-ad773e764135)

## Source Code
[Link to source code](https://github.com/michhandreaa/CSARCH2-Binary64FloatingPointConverterSimulationProject/)

## Analysis Writeup
1. <b>Error-catching different ways of writing positive numbers.</b>
- Although it sounds simple enough, one of the challenges that the team encountered while creating the app was the many different ways a user can write positive numbers. Thankfully, this problem was caught during the testing phase and solved by integrating it into the current data validation conditions.
2. <b>Implementing special cases</b>
- The hardest part that the team encountered was the implementation of special cases, although they may sound simple enough, given that these are values that have their own specific format. For some reason, it was difficult to catch these cases when we were following the process of converting to IEEE-754 Binary-64 format.
3. <b>Converting Decimal fractions to Binary</b>
- Another problem that the team encountered while creating the project was the proper way of converting decimal fractions to binary. During initial testing of the conversion, it seemed that the fraction converted correctly but looped multiple times. We tried converting the mantissa and the decimal exponent separately first, but this gave inaccurate results. Instead, we decided to transform the given decimal input so that the exponent in the scientific notation becomes 0, and this number will then be converted to binary and finally normalized.
4. <b>Converting Decimal exponent 10^n to its equivalent binary exponent 2<sup>m</sup></b>
- The team was also challenged to convert the decimal exponent directly to its equivalent binary exponent. The team searched different math and CS forums for a formula, but most were derivations that resulted in an approximation. It would’ve been fine, given that the approximations were more or less close enough to the actual exact supposed conversion. Sadly, it greatly affected the answer, and thus, the team had to look for a more concrete solution, which ended up converting the whole thing into binary instead and then normalizing the result.
5. <b>Radio buttons using Tkinder</b>
- During the creation of the GUI, there was an agreement regarding the use of radio buttons to choose between binary and decimal input and how their respective text boxes and text must appear depending on which was clicked. This proved to be a bit tricky to implement since Tkinter was an old GUI library and wasn’t really intuitive.
6. <b>Implementing the normalization function</b>
- In implementing the normalization function, the group experienced a problem getting the expected exponent, as there were instances wherein the exponent outputs were lacking or in excess of 1. However, the team was able to resolve this issue through a bit of tinkering and analyzing. 
