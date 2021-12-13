KEY = 1



def encode(value: str):
    result = ''
    for char in value:
        result += chr(ord(char) + KEY)

    return result


print(encode('1234'))
print(encode('abcd'))
print(encode('Vitalii'))


def decode(value: str):
    result = ''
    for char in value:
        result += chr(ord(char) - KEY)

    return result


print(decode('2345'))
print(decode('bcde'))
print(decode('Wjubmjj'))

'b1i8rcdpukaymrxouwxljeaabadyped9'