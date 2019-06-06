def rtod_converter(roman):
    roman_arr = [c for c in roman]
    for i,el in enumerate(roman_arr):
        if el == 'I':
            roman_arr[i]=1
        elif el == 'V':
            roman_arr[i]=5
        elif el == 'X':
            roman_arr[i]=10
        elif el == 'L':
            roman_arr[i]=50
        elif el == 'C':
            roman_arr[i]=100
        elif el == 'D':
            roman_arr[i]=500
        elif el == 'M':
            roman_arr[i]=1000
        else :
            roman_arr[i]=0
    anchor = max(roman_arr)
    flip = -1
    value = 0
    for i,el in enumerate(roman_arr):
        if el == anchor:
            flip = 1
        value += (flip) * el
    return value

if __name__=='__main__':
    print(rtod_converter(input()))