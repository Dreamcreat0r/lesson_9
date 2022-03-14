alph = []
char_code = ord('А')
while char_code <= ord('я'):
    alph.append(chr(char_code))
    char_code +=1 
print(alph)
index_little_yo = alph.index('ж')
alph.insert(index_little_yo, 'ё')
alph.insert(6, 'Ё')
print('\n\n\n\n', alph)