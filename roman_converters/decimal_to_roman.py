def dtor_converter(num):
    num_arr = [i for i in str(num)]
    num_arr = num_arr[::-1]
    roman_arr = []
    for i,el in enumerate(num_arr):
        if i == 0:
            unit = 'I'
            penta = 'V'
            deca = 'X'
        elif i == 1:
            unit = 'X'
            penta = 'L'
            deca = 'C'
        elif i == 2:
            unit = 'C'
            penta = 'D'
            deca = 'M'
        elif i == 3:
            unit = 'M'
            
        if el == '1':
            roman_arr.append(unit)
        elif el == '2':
            roman_arr.append(unit*2)
        elif el == '3':
            roman_arr.append(unit*3)
        elif el == '4':
            roman_arr.append(penta+unit)
        elif el == '5':
            roman_arr.append(penta)
        elif el == '6':
            roman_arr.append(unit+penta)
        elif el == '7':
            roman_arr.append((unit*2)+penta)
        elif el == '8':
            roman_arr.append((unit*3)+penta)
        elif el == '9':
            roman_arr.append(deca+unit)
        roman = ''.join(roman_arr)
    return(roman[::-1])

if __name__ == '__main__':
    print(dtor_converter(input()))