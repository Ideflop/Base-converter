#! /bin/python3

''' 
Todo:

binaire module et signe juste entier?
complement vrai juste entier
complement à 2 juste entier

Finish ? :

hex devrait fonctionnner de b et d en hex

'''
dec_convert = { # table convert from base <=16 to dec
"0": 0,
"1": 1,
"2": 2,
"3": 3,
"4": 4,
"5": 5,
"6": 6,
"7": 7,
"8": 8,
"9": 9,
"a": 10,
"b": 11,
"c": 12,
"d": 13,
"e": 14,
"f": 15,
}

def convert_to_dec(s, base=10, convert_table=dec_convert):
    ret = 0
    if "." not in s: 
        bef = s
    else: 
        bef, aft = s.split(".")
    
    for i in enumerate(reversed(bef)):
        integer = convert_table[i[1]]
        if integer >= base: 
            raise ValueError
        ret += base**i[0] * integer
    
    if "." not in s: 
        return ret

    for i in enumerate(aft):
        integer = convert_table[i[1]]
        if integer >= base: 
            raise ValueError
        ret += base**-(i[0] + 1) * integer

    return ret


def dec2bin(num):
    global whole_list
    global dec_list
    whole, dec = str(num).split('.')
    whole = int(whole)
    dec = int(dec)
    counter = 1
    
    while whole / 2 >= 1:
            i = int(whole % 2)
            whole_list.append(i)
            whole /= 2
            
    decproduct = dec      
    while counter <= 10:
        decproduct = decproduct * (10**-(len(str(decproduct))))
        decproduct *= 2
        decwhole, decdec = str(decproduct).split('.')
        decwhole = int(decwhole)
        decdec = int(decdec)
        dec_list.append(decwhole)
        decproduct = decdec
        counter += 1
        
whole_list = []
dec_list = []
f_list = []
dot = ['.']

def bin_dec(number):
    dec2bin(number)

    if(len(whole_list) > 1):
        whole_list.reverse()
    whole_list.insert(0, 1)

    f_list = whole_list + dot+ dec_list
    strings = [str(f_list) for f_list in f_list]
    return "".join(strings)

import struct

def binary(num): # convert dec into 32 bits
    return ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num)) # fonction from stackoverflow

def dec_to_hex(number):
    list_convert = []
    digit = number*(16**5) if isinstance(number, float) else number
    while digit > 16:
        list_convert.insert(0, int(digit % 16))
        digit //= 16
    list_convert.insert(0, digit % 16)
    list_convert[0] = int(list_convert[0])

    for i in range(len(list_convert)):
        if list_convert[i] >= 10:
            a = hex(list_convert[i])
            list_convert[i] = a[2:]

    list_string = [str(list_convert) for list_convert in list_convert]

    if isinstance(number, float):
        a = len(str(int(number)))
        list_string.insert(a, '.')

    return "".join(list_string)

def output(base,number):
    if base == 'b':

        print('Decimal :',convert_to_dec(number, 2)) # just dec
        print('Hexadecimal :', dec_to_hex(convert_to_dec(number, 2))) # just hex
        print('hexadecimal 8 bits :',hex(int(binary(float(convert_to_dec(number, 2))), 2))) # 8 bits

    elif base == 'd':

        print('Binaire :',bin_dec(float(number))) # just bin
        print('Binaire 32 bits :', binary(float(number))) # 32 bits
        print('Hexadecimal :', dec_to_hex(eval(number))) # just hex
        print('hexadecimal 8 bits :',hex(int(binary(float(number)), 2))) # 8 bits

    elif base == 'h':
        print('Decimal :',float.fromhex(number)) # just dec
        print('binaire :',bin_dec(float.fromhex(number))) # just bin
        print('Binaire 32 bits :', binary(float(float.fromhex(number)))) # 32 bin

    else:
        print(base, 'is not a valid base (b,d,h)')

if __name__ == "__main__":
    base = str(input('Input Base (b,d,h) :'))
    number = str(input('Digit :'))
    output(base, number)
