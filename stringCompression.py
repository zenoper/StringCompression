# // You should implement string compression algorithm

# // Algorithm should count repeated characters in source string
# // and return compressed string

# // If uncompressed string is shorter than compressed
# // algorithm should return uncompressed one

# // If source string contains numbers you need to throw an Error

# // e.g.
# // aaabbbccccc -> a3b3c5
# // aaabbccaa -> a3b2c2a2
# // abcd -> abcd

# // After implementation of compress function
# // you have to implement the decompressing algorithm

def compressString(string):
    empty_list = []
    compressed_list = []
    number_list = ['0', '1', '2', '3', '4', '5', '6', '8', '9']
    countOfRepeatedCharacters = 1

    for letter in string:
        if letter in empty_list:
            countOfRepeatedCharacters += 1
            repeatedLetter = letter + str(countOfRepeatedCharacters)
            compressed_list.pop()
            compressed_list.append(repeatedLetter)
        elif letter in number_list:
            raise TypeError('No numbers allowed in the string argument')
        else:
            countOfRepeatedCharacters = 1
            empty_list.clear()
            empty_list.append(letter)
            compressed_list.append(letter)
    compressed_string = ''.join(compressed_list)
    
    if len(compressed_string) > len(string):
        return string
    else:
        return compressed_string

print(compressString('aaabbbccccc'))
print(compressString('aaabbccaa'))
print(compressString('abc'))
print(compressString('a2'))
print(compressString(''))