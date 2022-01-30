#! /bin/python3

''' 
Todo:

integer dans h affiche resultat meme si dec est un float
bin_dec non plus, si nombre negatif on diplay - devant. integer utilse bin_dec

Fait:
convert_to_dec normalement pas non plus
dec_to_hex ne supporte pas nombre négatif
dec_convert pas besoin de lettre car fonction seulement utiliser pour converir en dec

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
"9": 9, # j'ai enlevé a = 10 etc normalement fc utiliser seulement convertir bin vers dec
}

def convert_to_dec(num, base=10, convert_table=dec_convert):
    negatif = False
    if '-' in num:
        num = num[1:]
        negatif = True

    ret = 0
    if "." not in num: 
        bef = num
    else: 
        bef, aft = num.split(".")
        
    for i in enumerate(reversed(bef)):
        integer = convert_table[i[1]]
        if integer >= base: 
            raise ValueError
        ret += base**i[0] * integer
    
    if "." not in num:
        if negatif:
            return eval('-'+str(ret)) 
        return ret

    for i in enumerate(aft):
        integer = convert_table[i[1]]
        if integer >= base: 
            raise ValueError
        ret += base**-(i[0] + 1) * integer

    if negatif:
        return eval('-'+str(ret))
    return ret


def dec2bin(num):
    global whole_list
    global dec_list
    whole_list = []
    dec_list = []
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
        

def bin_dec(num):
    dot = ['.']
    f_list = []
    dec2bin(num)

    if(len(whole_list) > 1):
        whole_list.reverse()
    whole_list.insert(0, 1)

    f_list = whole_list + dot+ dec_list
    strings = [str(f_list) for f_list in f_list]
    return "".join(strings)

import struct

def binary(num): # convert dec into 32 bits
    return ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num)) # fonction from stackoverflow

def dec_to_hex(num):
    negatif = False
    num = str(num)
    if '-' in num:
        num = num[1:]
        negatif = True
    num = eval(num)

    list_convert = []
    digit = num*(16**5) if isinstance(num, float) else num
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

    if isinstance(num, float):
        a = len(str(int(num)))
        list_string.insert(a, '.')
    
    if negatif:
        list_string.insert(0, '-')
    return "".join(list_string)

def integer(num, bit_size=8): # number = input  et bit = la taille du nombre à la fin
    init_number = eval(num)
    if '.' in num:
        return 'cannot convert flaot type'

    num = str(abs(int(num)))
    bit = bin_dec(float(26))
    bef, aft = bit.split(".")
    list_bit = list(bef)

    if len(list_bit) > bit_size:
        return 'bit format is smaller then the number in bit'
    count = len(list_bit)
    while count != bit_size:
        list_bit.insert(0, '0')
        count += 1
    if init_number < 0:
        list_bit[0] = '1'

    return "".join(list_bit)

def compl_vrai(number):
    l = integer(number, bit_size)
    l = list(str(l))
    for i in range(len(l)):
        l[i] = '0' if l[i]== '1' else '1'
    return "".join(l)

def compl_deux(number): 
    binary1 = "0b"+str(compl_vrai(number))
    binary2 = "0b1"
    integer_sum = int(binary1, 2) + int(binary2, 2)
    a = str(bin(integer_sum))
    return a[2:]

def output(base,number):
    if base == 'b':

        print('Decimal :',convert_to_dec(number, 2)) # just dec
        print('Hexadecimal :', dec_to_hex(convert_to_dec(number, 2))) # just hex
        print('hexadecimal 8 bits :',hex(int(binary(float(convert_to_dec(number, 2))), 2))) # 8 bits

    elif base == 'd':

        print('Binaire :',bin_dec(float(number))) # just bin
        print('Binaire 32 bits :', binary(float(number))) # 32 bits
        print(f'Binaire M&S {bit_size} bits :',integer(number, bit_size)) # M&S
        print('Binaire complément vrai :', compl_vrai(number))
        print('Binaire complément à 2 :', compl_deux(number))
        print('Hexadecimal :', dec_to_hex(number)) # just hex
        print('hexadecimal 8 bits :',hex(int(binary(float(number)), 2))) # 8 bits

    elif base == 'h':
        print('binaire :',bin_dec(float.fromhex(number))) # just bin
        print('Binaire 32 bits :', binary(float(float.fromhex(number)))) # 32 bin
        print(f'Binaire M&S {bit_size} bits :',integer(str(int(float.fromhex(number))), bit_size)) # M&S
        print('Binaire complément vrai :', compl_vrai(str(int(float.fromhex(number)))))
        print('Binaire complément à 2 :', compl_deux(str(int(float.fromhex(number)))))
        print('Decimal :',float.fromhex(number)) # just dec

    else:
        print(base, 'is not a valid base (b,d,h)')

if __name__ == "__main__":
    base = str(input('Input Base (b,d,h) :'))
    number = str(input('Digit :'))
    bit_size = eval(input('Input the bit size for the binary number :'))
    output(base, number)
