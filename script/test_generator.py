import random

# test generator
def generate_test(type, width, height):
    start_sym = u''
    size = 0

    if (type == 'rus'):
        start_sym = u'а'
        size = 33
    elif (type == 'num'):
        start_sym = u'0'
        size = 10
    else:
        return None

    matrix = generate_symbol_matrix(start_sym, size, width, height)
    test_symbol1 = chr(random.randint(ord(start_sym), ord(start_sym) + size))
    test_symbol2 = chr(random.randint(ord(start_sym), ord(start_sym) + size))
    while (test_symbol1 == test_symbol2):
        test_symbol2 = chr(random.randint(ord(start_sym), ord(start_sym) + size))

    return matrix, (test_symbol1, test_symbol2)


# Test matrix generator
def generate_symbol_matrix(offset, size, width, height):
    offset_start_pos = ord(offset)
    offset_end_pos = offset_start_pos + size

    matrix = []
    for i in range(height):
        string = []
        for j in range(width):
            prom = random.randint(offset_start_pos, offset_end_pos - 1)
            string.append(chr(prom))
        matrix.append(string)
    return matrix


# Testing
# matrix, symbols = generate_test('rus', 10, 5)
# for string in matrix:
#     print(string)
# print(symbols)