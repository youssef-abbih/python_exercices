str1 = input('str1: ')
str2 = input('str2: ')

count = 0
if len(str1) == len(str2):
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            count +=1
    print(f"La distance de Hamming entre {str1} et {str2} est {count}")
else:
    print('Les chaines doivent avoir la même taille')

