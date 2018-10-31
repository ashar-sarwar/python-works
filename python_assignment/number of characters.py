dictionary = {}
line=input("Enter line Here:  ")

for alpha in line:
    dictionary[alpha] = dictionary.get(alpha,0)+1

print('\n'.join(['%s,%i' % (k, v) for k, v in dictionary.items()]))

