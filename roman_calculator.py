'''
Arguments: str(roman numeral A), str(operator), str(roman numeral B)
Output: str(Solution to the expression in Roman)
-sohailshaukat ( https://github.com/sohailshaukat )
-sohail47k@gmail.com
'''

from roman_converters import roman_to_decimal, decimal_to_roman

def calculator(num1 ,num2, op):
    if op == '+':
        result = num1+num2
    if op == '-':
        result = num1-num2
    if op == '*':
        result = num1*num2
    if op == '/':
        if not num2 == 0:
            result = int(num1/num2)
        else:
            print("Second Number can not be zero")
            return
    return result

if __name__ == "__main__":
    roman1 = str(input())
    operation = str(input())
    roman2 = str(input())
    num1 = roman_to_decimal.rtod_converter(roman1)
    num2 = roman_to_decimal.rtod_converter(roman2)
    operation = operation[0]
    result_decimal = calculator(num1, num2, operation)
    result_roman = decimal_to_roman.dtor_converter(result_decimal)
    print(result_roman)


# def rtod_converter(roman):
#     roman_arr = [c for c in roman]
#     for i,el in enumerate(roman_arr):
#         if el == 'I':
#             roman_arr[i]=1
#         elif el == 'V':
#             roman_arr[i]=5
#         elif el == 'X':
#             roman_arr[i]=10
#         elif el == 'L':
#             roman_arr[i]=50
#         elif el == 'C':
#             roman_arr[i]=100
#         elif el == 'D':
#             roman_arr[i]=500
#         elif el == 'M':
#             roman_arr[i]=1000
#         else :
#             roman_arr[i]=0
#     anchor = max(roman_arr)
#     flip = -1
#     value = 0
#     for i,el in enumerate(roman_arr):
#         if el == anchor:
#             flip = 1
#         value += (flip) * el
#     return value

# def dtor_converter(num):
#     num_arr = [i for i in str(num)]
#     num_arr = num_arr[::-1]
#     roman_arr = []
#     for i,el in enumerate(num_arr):
#         if i == 0:
#             unit = 'I'
#             penta = 'V'
#             deca = 'X'
#         elif i == 1:
#             unit = 'X'
#             penta = 'L'
#             deca = 'C'
#         elif i == 2:
#             unit = 'C'
#             penta = 'D'
#             deca = 'M'
#         elif i == 4:
#             unit = 'M'

#         if el == '1':
#             roman_arr.append(unit)
#         elif el == '2':
#             roman_arr.append(unit*2)
#         elif el == '3':
#             roman_arr.append(unit*3)
#         elif el == '4':
#             roman_arr.append(penta+unit)
#         elif el == '5':
#             roman_arr.append(penta)
#         elif el == '6':
#             roman_arr.append(unit+penta)
#         elif el == '7':
#             roman_arr.append((unit*2)+penta)
#         elif el == '8':
#             roman_arr.append((unit*3)+penta)
#         elif el == '9':
#             roman_arr.append(deca+unit)
#         roman = ''.join(roman_arr)
#     return(roman[::-1])
