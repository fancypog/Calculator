# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 13:57:03 2023

@author: Frances
"""
# =============================================================================
# Solution
# =============================================================================

# #============================================================================
# # Uncomment this block to test one expression step by step!
#
# expression = ('/ - 3 4 + 5 2')
#
# #============================================================================

# Fist, define a function that calculates using the alternative notation
# Alternate calculate: operator, operand1, operand2
def altCalculate(operator, operand1, operand2):
    operand1 = int(operand1)
    operand2 = int(operand2)
    # Perform the calculation based on the operator
    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        result = operand1 / operand2
    
    return result

# Define the main function that takes the alternative solution and outputs the result
def calculate(expression):
    # Remove whitespace characters from the expression
    expression = ''.join(expression.split())
    # Tranverse through the expression and split it into sub calculations.
    # Operator, sub-calculation1, subcalculation2
    # Operands: either one numeric character 
    # or a sub-calculation of one operator with the following two numeric characters
    operator = expression[0] # The first character is an operator of the main calculation
    operators = ['+', '-', '*', '/']
    # 1. If the expression has three characters, calculate it directly
    if len(expression) == 3: 
        return altCalculate(expression[0], expression[1], expression[2])
    # 2. If the expression has five characters, it contains one number and one sub-calculation
    elif len(expression) == 5:
        if expression[1] in operators:
            # Expression format: Operator, Operand1(sub-calculation), Operand2(a number)
            operand1 = expression[1:4]
            operand2 = expression[4:]
            subCal1 = altCalculate(operand1[0], operand1[1], operand1[2])
            subCal2 = operand2
        else:
            # Expression format: Operator, Operand1(a number), Operand2(sub-calculation)
            operand1 = expression[1]
            operand2 = expression[2:]
            subCal1 = operand1
            subCal2 = altCalculate(operand2[0], operand2[1], operand2[2])
        return altCalculate(operator, subCal1, subCal2)
    # 3. If the expression has seven characters, it contains two sub-calculations
    elif len(expression) == 7:
        # Split
        if expression[1] in operators:
            # Expression format: Operator, Operand1(sub-calculation), Operand2(sub-calculation)
            operand1 = expression[1:4]
            operand2 = expression[4:]
            subCal1 = altCalculate(operand1[0], operand1[1], operand1[2])
            subCal2 = altCalculate(operand2[0], operand2[1], operand2[2])

        return altCalculate(operator, subCal1, subCal2)
         
# =============================================================================
# Tests
# =============================================================================
# Test the following alternative notations and print the results
altNot = ['+ 3 4', '- 3 * 4 5', '* + 3 4 5', '/ - 3 4 + 5 2']

for expression in altNot:
    result = calculate(expression)
    print(f"Expression: {expression}, Result: {result}")


